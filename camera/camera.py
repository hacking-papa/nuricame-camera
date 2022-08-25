import picamera


class Camera:
    def shoot(self, filename: str = "input.jpg"):
        with picamera.PiCamera() as camera:
            camera.resolution = (512, 512)
            camera.capture(filename)
            return True


if __name__ == "__main__":
    Camera().snap()
