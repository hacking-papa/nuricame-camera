#!/usr/bin/env python3

import config
import paperang_hardware as hardware
import paperang_image_data as image_data
import skimage as ski


class Paperang_Printer:
    def __init__(self):
        self.printer_hardware = hardware.Paperang(
            config.get("DEFAULT", "printer_mac_address")
        )

    def print_self_test(self):
        printer_mac_address = config.get("DEFAULT", "printer_mac_address")
        print(f"attempting test print to MAC address: {printer_mac_address}")
        if self.printer_hardware.connected:
            self.printer_hardware.sendSelfTestToBt()

    def print_image_file(self, path):
        if self.printer_hardware.connected:
            self.printer_hardware.sendImageToBt(
                image_data.binimage2bitstream(
                    image_data.im2binimage(ski.io.imread(path), conversion="threshold")
                )
            )

    def print_dithered_image(self, path):
        if self.printer_hardware.connected:
            self.printer_hardware.sendImageToBt(image_data.im2binimage2(path))


if __name__ == "__main__":
    mmj = Paperang_Printer()
    mmj.print_self_test()
    # mmj.print_image_file("output.jpg")
