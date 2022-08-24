import picamera


class Camera:
    def snap(filename: str = "input.jpg"):
        camera = picamera.PiCamera()
        camera.capture(filename, resize=(512, 512))


if __name__ == "__main__":
    Camera().snap()
