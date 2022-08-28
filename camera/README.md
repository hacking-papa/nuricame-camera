# nuricame-camera - Camera

Make a contour by pictures, version with separated camera.

- [Prerequisites](#prerequisites)
- [How to](#how-to)
  - [Setup](#setup)
    - [Raspbian](#raspbian)
      - [VNC](#vnc)
    - [Lipo SHIM](#lipo-shim)
    - [Camera](#camera)
    - [I2C Display](#i2c-display)
    - [Thermal Printer](#thermal-printer)
    - [Enclosure](#enclosure)
  - [Use](#use)
    - [Auto Start using Systemd](#auto-start-using-systemd)
    - [Check](#check)
      - [SCP](#scp)
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

If you want to rotate the image to be taken, set the angle in config.py.

#### I2C Display

See [1.3inch LCD HAT - Waveshare Wiki](https://www.waveshare.com/wiki/1.3inch_LCD_HAT).

Run `setup.sh` to install all dependencies automatically.

#### Thermal Printer

First, you should find the device, `sudo hcitool scan`.

#### Enclosure

(T. B. D.)

### Use

```shell
cd /home/pi/Workspace/nuricame-camera/camera && python main.py
```

#### Auto Start using Systemd

```/etc/systemd/system/nuricame-camera.service
[Unit]
Description=nuricame camera program
After=network.target

[Service]
WorkingDirectory=/home/pi/Workspace/nuricame-camera/camera
ExecStart=/usr/bin/python3 /home/pi/Workspace/nuricame-camera/camera/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

#### Check

##### SCP

To download images from Raspberry Pi, `scp pi@nuricame-02.local:/home/pi/Workspace/nuricame-camera/camera/output.jpg ~/Downloads`

## Misc

### License

The software is distributed freely under **GOOD DADDY LICENSE**, see [LICENSE](LICENSE).
