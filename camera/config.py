import configparser

config = configparser.ConfigParser()

config["DEFAULT"] = {
    "debug": True,
    "camera_rotation": 90,
    "camera_meter_mode": "average",
    "server_url": "192.168.100.9",
    "server_port": "8000",
    "printer_mac_address": "00:15:83:B7:0E:91",
}
