import requests
from PIL import Image
from io import StringIO


def main(path: str):
    url = "http://192.168.100.9:8000/"
    file = {"file": open(path, mode="rb")}
    res = requests.post(url, files=file)
    print(res)
    img = Image.open(StringIO(res.content))
    img.save("output.jpg")


if __name__ == "__main__":
    main("../server/samples/Airplane.jpg")
