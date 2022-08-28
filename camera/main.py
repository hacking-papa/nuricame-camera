#!/usr/bin/env python3

from datetime import datetime
import os
import socket

import RPi.GPIO as GPIO
import spidev as SPI
import ST7789
from loguru import logger
from PIL import Image, ImageDraw, ImageFont
from uploader import Uploader

from camera import Camera
from paperang_printer import Paperang_Printer

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

def get_absolute_path():
    return os.path.dirname(os.path.abspath(__file__))

def get_postfix():
    now = datetime.now()
    return now.strftime("%Y%m%d%H%M%S")


def get_hostname():
    return socket.gethostname()


def get_ip_address():
    connect_interface = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connect_interface.connect(("8.8.8.8", 80))
    return connect_interface.getsockname()[0]


def main():
    logger.add("logs/{time}.log", rotation="1 day")
    logger.info("Start")

    display = ST7789.ST7789(SPI.SpiDev(bus, device), RST, DC, BL)
    display.Init()
    display.clear()

    # GPIO Initialize
    GPIO.setmode(GPIO.BCM)
    # GPIO.setup(KEY_UP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
    # GPIO.setup(KEY_DOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # GPIO.setup(KEY_LEFT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # GPIO.setup(KEY_RIGHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KEY_PRESS_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # GPIO.setup(KEY1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # GPIO.setup(KEY2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # GPIO.setup(KEY3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    font = ImageFont.truetype("fonts/mononoki.ttf", 24)
    # Prepare Home Image
    home_img = Image.open("home_240x240.png")
    home_draw = ImageDraw.Draw(home_img)

    home_draw.text((0, 0), get_hostname(), font=font, fill=(255, 255, 255))
    # home_draw.text((0, 30), get_ip_address(), font=font, fill=(255, 255, 255))
    display.ShowImage(home_img, 0, 0)

    while True:
        """Main Routine"""
        if not GPIO.input(KEY_PRESS_PIN):
            postfix = get_postfix()
            input_filename = f"{get_absolute_path()}/camera_{postfix}.jpg"
            output_filename = f"{get_absolute_path()}/output_{postfix}.jpg"
            if Camera().shoot(input_filename):
                logger.info(f"Successful shooting: {input_filename}")
                display.clear()
                input_img = Image.open(input_filename).resize(
                    (display_width, display_height)
                )
                display.ShowImage(input_img, 0, 0)
                if Uploader().upload(
                    upload_filename=input_filename, output_filename=output_filename
                ):
                    logger.info(
                        f"Successful uploading: {input_filename} -> {output_filename}"
                    )
                Paperang_Printer().print_image_file(output_filename)
                logger.info(f"Successful printing: {output_filename}")
                display.clear()
                display.ShowImage(home_img, 0, 0)


if __name__ == "__main__":
    main()
