import picamera
from config import config


class Camera:
    def shoot(self, filename: str = "input.jpg"):
        with picamera.PiCamera() as camera:
            camera.resolution = (512, 512)
            camera.rotation = config.getint("DEFAULT", "camera_rotation")
            camera.meter_mode = config.get(
                "DEFAULT", "camera_meter_mode", fallback="average"
            )
            camera.capture(filename)
            return True


if __name__ == "__main__":
    Camera().shoot()
