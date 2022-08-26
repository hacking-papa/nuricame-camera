import numba
import numpy as np
import skimage as ski
from PIL import Image, ImageEnhance


def _pack_block(bits_str: str) -> bytearray:
    """Pack a string of bits into a block of bytes.

    Args:
        bits_str (str): human way (MSB:LSB) of representing binary numbers (e.g. "1010" means 12)

    Returns
        bytearray: packed bits
    """
    if len(bits_str) % 8 != 0:
        raise ValueError("bits_str should have the length of ")
    partitioned_str = [bits_str[i : i + 8] for i in range(0, len(bits_str), 8)]
    int_str = [int(i, 2) for i in partitioned_str]
    return bytes(int_str)


def binimage2bitstream(bin_image: np.ndarray):
    """input follows thermal printer's mechanism: 1 is black (printed) and 0 is white (left untouched)

    Args:
        bin_image (np.ndarray): numpy int array consists of only 1s and 0s

    Returns:
        _type_: _description_
    """
    # bin_image is a numpy int array consists of only 1s and 0s
    # input follows thermal printer's mechanism: 1 is black (printed) and 0 is white (left untouched)
    assert bin_image.max() <= 1 and bin_image.min() >= 0
    return _pack_block("".join(map(str, bin_image.flatten())))


def im2binimage(im, conversion="threshold"):
    # convert standard numpy array image to bin_image
    fixed_width = 384

    if len(im.shape) != 2:
        im = ski.color.rgb2gray(im)
    im = ski.transform.resize(
        im, (round(fixed_width / im.shape[1] * im.shape[0]), fixed_width)
    )
    if conversion == "threshold":
        ret = (im < ski.filters.threshold_li(im)).astype(int)
    elif conversion == "edge":
        ret = 1 - (1 - (ski.feature.canny(im, sigma=2)))
    else:
        raise ValueError("Unsupported conversion method")
    return ret


# this is straight from https://github.com/tgray/hyperdither
@numba.jit
def dither(num, thresh=127):
    derr = np.zeros(num.shape, dtype=int)

    div = 8
    for y in range(num.shape[0]):
        for x in range(num.shape[1]):
            newval = derr[y, x] + num[y, x]
            if newval >= thresh:
                errval = newval - 255
                num[y, x] = 1.0
            else:
                errval = newval
                num[y, x] = 0.0
            if x + 1 < num.shape[1]:
                derr[y, x + 1] += errval / div
                if x + 2 < num.shape[1]:
                    derr[y, x + 2] += errval / div
            if y + 1 < num.shape[0]:
                derr[y + 1, x - 1] += errval / div
                derr[y + 1, x] += errval / div
                if y + 2 < num.shape[0]:
                    derr[y + 2, x] += errval / div
                if x + 1 < num.shape[1]:
                    derr[y + 1, x + 1] += errval / div
    return num[::-1, :] * 255


def im2binimage2(im):
    basewidth = 384
    # resizer = pilkit.processors.ResizeToFit(fixed_width)
    # import in B&W, probably does not matter
    img = Image.open(im).convert("L")
    # img = Image.open(im)
    # img.show()

    wpercent = basewidth / float(img.size[0])
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    # img.save('test.pgm', format="PPM")
    # os.system('pamditherbw -atkinson test.pgm > test2.pgm')
    # os.system('pamtopnm <test2.pgm >test3.pbm')
    # img2 = Image.open('/Users/ktamas/Prog/python-paperang/test3.pbm')
    # img2 = Image.open('test3.pbm').convert('1')
    # img2.show()
    # os.system('')

    # img.show()
    # resize to the size paperang needs
    # new_img = resizer.process(img)
    # new_img.show()
    # do atkinson dithering
    # s = atk.atk(img.size[0], img.size[1], img.tobytes())
    # o = Image.frombytes('L', img.size, s)
    # o = Image.fromstring('L', img.size, s)

    m = np.array(img)[:, :]
    m2 = dither(m)
    # out = Image.fromarray(m2[::-1,:]).convert('1')
    out = Image.fromarray(m2[::-1, :])
    out.show()
    # the ditherer is stupid and does not make black and white images, just... almost so this fixes that
    enhancer = ImageEnhance.Contrast(out)
    enhanced_img = enhancer.enhance(4.0)
    enhanced_img.show()
    # now convert it to true black and white
    # blackandwhite_img = enhanced_img.convert('1')
    # blackandwhite_img.show()
    np_img = np.array(enhanced_img).astype(int)
    # flipping the ones and zeros
    np_img[np_img == 1] = 100
    np_img[np_img == 0] = 1
    np_img[np_img == 100] = 0

    return binimage2bitstream(np_img)


def sirius(im):
    np_img = np.fromfile(im, dtype="uint8")
    # there must be a less stupid way to invert the array but i am baby
    np_img[np_img == 1] = 100
    np_img[np_img == 0] = 1
    np_img[np_img == 100] = 0
    return binimage2bitstream(np_img)
