from io import BytesIO
import requests
from PIL import Image
from config import config


class Uploader:
    def upload(self, upload_file: str):
        url = config.get("DEFAULT", "server_url")
        file = {"file": open(upload_file, mode="rb")}
        response = requests.post(url, files=file)
        print(response)
        if response.status_code is 200:
            img = Image.open(BytesIO(response.content))
            img.save("output.jpg")
            return True
        else:
            return False


if __name__ == "__main__":
    Uploader().upload("input.jpg")
