from io import BytesIO
import requests
from PIL import Image
from config import config


def main(path: str):
    url = config.get("DEFAULT", "server_url")
    file = {"file": open(path, mode="rb")}
    res = requests.post(url, files=file)
    print(res)
    if res.status_code is 200:
        img = Image.open(BytesIO(res.content))
        img.save("output.jpg")


if __name__ == "__main__":
    main("../server/samples/Airplane.jpg")
