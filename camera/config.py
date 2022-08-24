import configparser

config = configparser.ConfigParser()

config["DEFAULT"] = {
    "server_url": "http://192.168.100.9:8000/",
    "printer_mac_address": "00:00:00:00:00:00",
}
