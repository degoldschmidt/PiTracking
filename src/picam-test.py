import time
import picamera
from io import BytesIO

frames = 5
stream = BytesIO()
def filenames():
    frame = 0
    while frame < frames:
        yield '../../out/image%02d.jpg' % frame
        frame += 1

with picamera.PiCamera() as camera:
    camera.resolution = (900, 900)
    camera.framerate = 30
    camera.start_preview()
    # Give the camera some warm-up time
    time.sleep(2)
    start = time.time()
    camera.start_recording("../../out/out.h264")
    camera.wait_recording(30)
    camera.stop_recording()
    finish = time.time()
print('Captured %d frames at %.2ffps' % (
    frames,
    frames / (finish - start)))
