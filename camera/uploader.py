from io import BytesIO

import requests
from config import config
from PIL import Image


class Uploader:
    def upload(self, upload_filename: str, output_filename: str = "output.jpg"):
        url = config.get("DEFAULT", "server_url")
        file = {"file": open(upload_filename, mode="rb")}
        response = requests.post(url, files=file)
        print(response)
        if response.status_code is 200:
            img = Image.open(BytesIO(response.content))
            img.save(output_filename)
            return True
        else:
            return False


if __name__ == "__main__":
    Uploader().upload("home_240x240.png")
