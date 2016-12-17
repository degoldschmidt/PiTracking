from threading import Thread
import cv2

class CVVideoCapture:
    """ The CVVideoCapture class creates a threaded OpenCV video capture.
    AUTHOR:  Dennis Goldschmidt
    CREATED: 16/12/2016
    UPDATED: 
    """

    def __init__(self, source=0, verbose=False):
        """ Constructor """

        self._VERBOSE = verbose
        # opencv video capture
        (print("Video Source:", source)) if self._VERBOSE else 0
        self.cap = cv2.VideoCapture(source)
        # initial frame grab
        (self.grabbed, self.frame) = self.cap.read()
        # capture breaking condition
        self.stopping = False

    def display(self):
        cv2.imshow("Live", frame)
        cv2.moveWindow("Live", 0, 0)

    def get(self):
        """ return latest frame """
        return self.frame

    def run(self):
        """ start and run a thread for grabbing frames from capture """
        thr = Thread(target=self.update, args=())
        thr.daemon = True #### find out about this
        thr.start()
        return self

    def stop(self):
        """ stops video capture """
        self.stopping = True

    def update(self):
        """ update frame from capture """
        # indefinite until break
        while True:
            # stopping condition
            if self.stopping:
                return
            # grab frame
            (self.grabbed, self.frame) = self.cap.read()

import time
_DISPLAY = True
_NFRAMES = 200
testcap = CVVideoCapture().run()
start_t = time.time()
for i in range(_NFRAMES):
    frame = testcap.get()
    if _DISPLAY:
        testcap.display()
    key = cv2.waitKey(1)
    now = time.time()-start_t
    #print("Frame:", i, "@", now, "secs")
        
print("Approx. frame rate:", _NFRAMES/now, "fps")
cv2.destroyAllWindows()
testcap.stop()
    
