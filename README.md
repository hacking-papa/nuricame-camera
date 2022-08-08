# nuricame-camera

Make a contour by pictures, version with separeted camera.

- [Prerequisites](#prerequisites)
- [How to](#how-to)
  - [Setup](#setup)
    - [Raspbian](#raspbian)
      - [VNC](#vnc)
    - [Lipo SHIM](#lipo-shim)
    - [Camera](#camera)
    - [I2C Display](#i2c-display)
- [Enclosure](#enclosure)
- [Misc](#misc)
  - [License](#license)

## Prerequisites

- Raspberry Pi Zero 2W (Bullseye 32bit)
  - [Lipo SHIM](https://shop.pimoroni.com/products/lipo-shim?variant=23979864391)
  - [1.3" TFT LCD](https://www.waveshare.com/wiki/1.3inch_LCD_HAT)

## How to

### Setup

#### Raspbian

It is useful to enable SSH when creating SD card images.

##### VNC

It is even better if VNC is also enabled after startup.

The encryption should be `Prefer off` and the authentication method should be `VNC password` so that the connection can be made from the MacOS standard Screen Sharing.

#### Lipo SHIM

See [pimoroni/clean-shutdown](https://github.com/pimoroni/clean-shutdown).

Run `setup.sh` to install the daemon automatically.

If you want to do it manually, run `./zerolipo.sh`.

#### Camera

(T. B. D.)

#### I2C Display

See [1.3inch LCD HAT - Waveshare Wiki](https://www.waveshare.com/wiki/1.3inch_LCD_HAT).

Run `setup.sh` to install all dependencies automatically.

## Enclosure

(T. B. D.)

## Misc

### License

The software is distributed freely under **GOOD DADDY LICENSE**, see [LICENSE](LICENSE).
