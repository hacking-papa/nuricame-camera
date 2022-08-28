import configparser

config = configparser.ConfigParser()

config["DEFAULT"] = {
    "camera_rotation": 90,
    "server_url": "192.168.100.9",
    "server_port": "8000",
    "printer_mac_address": "00:15:83:B7:0E:91",
}
