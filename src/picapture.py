# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread
import cv2
import time


class PiVideoCapture:
    """ The PiVideoCapture class creates a threaded picamera video capture.
    AUTHOR:  Dennis Goldschmidt
    CREATED: 19/12/2016
    UPDATED:
    """

    def __init__(self, resolution=(1920, 1072), framerate=30):
        # initialize the camera and stream
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.cap_raw = PiRGBArray(self.camera, size=resolution)
        self.cap = self.camera.capture_continuous(
            self.cap_raw, format="bgr", use_video_port=True)

        # initialize the frame and the variable used to indicate
        # if the thread should be stopped
        self.frame = None
        self.stopping = False

    def display(self):
        self.camera.start_preview()
        time.sleep(2)

    def get(self):
        """ return latest frame """
        return self.frame

    def run(self):
        """ start and run a thread for grabbing frames from capture """
        print("Run thread")
        thr = Thread(target=self.update, args=())
        thr.daemon = True
        thr.start()
        return self

    def stop(self):
        """ stop video capture """
        self.stopping = True

    def update(self):
        """ update frame from capture """
        print("Update thread")
        # keep looping infinitely until the thread is stopped
        for f in self.cap_raw:
            # grab the frame from the stream and clear the stream in
            # preparation for the next frame
            self.frame = f.array
            self.cap_raw.truncate(0)

            # if the thread indicator variable is set, stop the thread
            # and resource camera resources
            if self.stopping:
                self.cap.close()
                self.cap_raw.close()
                self.camera.close()
                return

"""
import time
_DISPLAY = True
_NFRAMES = 200
testcap = PiVideoCapture().run()
start_t = time.time()
if _DISPLAY:
    testcap.display()
for i in range(_NFRAMES):
    frame = testcap.get()
    print(i)
    now = time.time() - start_t
    #print("Frame:", i, "@", now, "secs")

print("Approx. frame rate:", _NFRAMES / now, "fps")
cv2.destroyAllWindows()
testcap.stop()
"""
