from threading import Thread
import cv2

class CVVideoCapture:
    """ The CVVideoCapture class creates a threaded OpenCV video capture.
    AUTHOR:  Dennis Goldschmidt
    CREATED: 16/12/2016
    UPDATED:
    """

    def __init__(self, source=1, verbose=True, size=(1200,800)):
        """ Constructor """

        self._VERBOSE = verbose
        self.size = size
        # opencv video capture
        print("Video Source:", source) if self._VERBOSE else 0
        self.cap = cv2.VideoCapture(source)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])
        self.cap.set(cv2.CAP_PROP_FPS, 20)
        print("W:",self.cap.get(3)) if self._VERBOSE else 0
        print("H:",self.cap.get(4)) if self._VERBOSE else 0
        print("FPS:",self.cap.get(5)) if self._VERBOSE else 0
        # initial frame grab
        (self.grabbed, self.frame) = self.cap.read()
        # capture breaking condition
        self.stopping = False

    def display(self):
        print(self.size)
        downsize = self.size
        w,h = int(0.25 *downsize[0]), int(0.25 *downsize[1]) 
        rsframe = cv2.resize(self.frame, (w, h))
        cv2.imshow("Live", rsframe)
        cv2.moveWindow("Live", 0, 0)

    def get(self):
        """ return latest frame """
        return self.frame

    def getProperty(self, index):
        """ return capture properties """
        return self.cap.get(index)

    def run(self):
        """ start and run a thread for grabbing frames from capture """
        thr = Thread(target=self.update, args=())
        thr.daemon = True #### find out about this
        thr.start()
        return self

    def setBrightness(self, value):
        print(value)
        self.cap.set(cv2.CAP_PROP_BRIGHTNESS,value)
        print("Brightness:",self.cap.get(cv2.CAP_PROP_BRIGHTNESS))

    def setContrast(self, value):
        print(value)
        self.cap.set(cv2.CAP_PROP_CONTRAST,value)
        print("Contrast:",self.cap.get(cv2.CAP_PROP_CONTRAST))

    def setExposure(self, value):
        print(value)
        self.cap.set(cv2.CAP_PROP_EXPOSURE,value)
        print("Exposure:",self.cap.get(cv2.CAP_PROP_EXPOSURE))

    def setFramerate(self, value):
        print(value)
        self.cap.set(cv2.CAP_PROP_FPS,value)
        print("Frame rate:",self.cap.get(cv2.CAP_PROP_FPS))

    def setGain(self, value):
        print(value)
        self.cap.set(cv2.CAP_PROP_GAIN,value)
        print("Gain:",self.cap.get(cv2.CAP_PROP_GAIN))

    def setHeight(self, value):
        print(value)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,value)
        print("Frame height:", self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def setHue(self, value):
        print(value)
        self.cap.set(cv2.CAP_PROP_HUE,value)
        print("Hue:",self.cap.get(cv2.CAP_PROP_HUE))

    def setSaturation(self, value):
        print(value)
        self.cap.set(cv2.CAP_PROP_SATURATION,value)
        print("Saturation:", self.cap.get(cv2.CAP_PROP_SATURATION))

    def setWidth(self, value):
        print(value)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, value)
        print("Frame width:", self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    def stop(self):
        """ stop video capture """
        self.stopping = True

    def update(self):
        """ update frame from capture """
        # indefinite until stop
        while not self.stopping and self.cap.isOpened():
            # grab frame
            (self.grabbed, self.frame) = self.cap.read()

def main():
    import time
    _DISPLAY = True
    _NFRAMES = 100
    _FPS = 30
    _PERIOD = 1/_FPS
    testcap = CVVideoCapture(size=(1280, 1024)).run()
    start_t = time.time()
    last_t = time.time()
    for i in range(_NFRAMES):
        frame = testcap.get()
        if _DISPLAY:
            testcap.display()
            cv2.waitKey(1)
        else:
            delta_t = time.time() - last_t
            key = cv2.waitKey(int(1000*(_PERIOD - delta_t)))
        last_t = time.time()
        now = time.time()-start_t
        #print("Frame:", i, "@", now, "secs")

    print("Approx. frame rate:", _NFRAMES/now, "fps")
    cv2.destroyAllWindows()
    testcap.stop()
    
if __name__ == '__main__':
    main()

