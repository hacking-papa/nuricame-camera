import spidev as SPI
from camera.ST7789 import ST7789
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont


# GPIO define

RST_PIN = 25
CS_PIN = 8
DC_PIN = 24

KEY_UP_PIN = 6
KEY_DOWN_PIN = 19
KEY_LEFT_PIN = 5
KEY_RIGHT_PIN = 26
KEY_PRESS_PIN = 13

KEY1_PIN = 21
KEY2_PIN = 20
KEY3_PIN = 16

RST = 27
DC = 25
BL = 24

bus = 0
device = 0

display_width = 240
display_height = 240


def main():
    display = ST7789.ST7789(SPI.SpiDev(bus, device), RST, DC, BL)
    display.Init()
    display.clear()

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(KEY_UP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
    GPIO.setup(KEY_DOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KEY_LEFT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KEY_RIGHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KEY_PRESS_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KEY1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KEY2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KEY3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    image = Image.new("RGB", (display_width, display_height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, display_width, display_height), fill=(0, 0, 0))
    draw.ShowImage(image, 0, 0)

    # TODO: implement key event handler
    # TODO: implement image capture
    # TODO: implement image display
    # TODO: implement upload image
    # TODO: implement print image


if __name__ == "__main__":
    main()
