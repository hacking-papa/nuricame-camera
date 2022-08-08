# nuricame-camera

Make a contour by pictures, version with separeted camera.

- [Prerequisites](#prerequisites)
- [How to](#how-to)
  - [Setup](#setup)
    - [Raspbian](#raspbian)
    - [Lipo SHIM](#lipo-shim)
    - [Camera](#camera)
    - [I2C Display](#i2c-display)
- [Enclosure](#enclosure)
- [Misc](#misc)
  - [License](#license)

## Prerequisites

- Raspberry Pi Zero 2W (Bullseye 32bit)
  - Lipo SHIM
  - 1.3" TFT LCD

## How to

### Setup

#### Raspbian

It is useful to enable SSH when creating SD card images.
It is even better if VNC is also enabled after startup.

#### Lipo SHIM

Run `setup.sh` to install the daemon automatically.

If you want to do it manually, run `./zerolipo.sh`.

#### Camera

(T. B. D.)

#### I2C Display

Run `setup.sh` to install all dependencies automatically.

## Enclosure

(T. B. D.)

## Misc

### License

The software is distributed freely under **GOOD DADDY LICENSE**, see [LICENSE](LICENSE).
