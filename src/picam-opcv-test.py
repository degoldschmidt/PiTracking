import picamera
import picamera.array
import time
import cv2
import numpy as np

with picamera.PiCamera() as camera:
    camera.resolution = (1920, 1080)
    camera.framerate = 30
    time.sleep(2) # AGC warm-up time
    start = time.time()
    for i in range(30):
        with picamera.array.PiRGBArray(camera) as stream:
            camera.capture(stream, 'bgr', use_video_port=True)
            #hsv = cv2.cvtColor(stream.array, cv2.COLOR_BGR2HSV)
    finish = time.time()
    print('Processed 24 frames in', finish - start, ' seconds at', camera.framerate/(finish - start),' fps')
