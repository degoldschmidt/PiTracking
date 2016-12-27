class VideoCapture:
    """ The generic VideoCapture class creates a threaded video capture using either OpenCV or PiCamera.
    AUTHOR:  Dennis Goldschmidt
    CREATED: 20/12/2016
    UPDATED:
    """

    def __init__(self, cap_type, source=0, resolution=(1920, 1080), framerate=30, verbose=False):
        """ Constructor """

        self._VERBOSE = verbose
        print("Capture type:", cap_type) if self._VERBOSE else 0
        print("Video Source:", source) if self._VERBOSE else 0

        if cap_type == "CV":
            from cvcapture import CVVideoCapture
            self.cap = CVVideoCapture(source)
        elif cap_type == "PI":
            from picapture import PiVideoCapture
            self.cap = PiVideoCapture(resolution, framerate)
        else:
            print("ERROR: Capture type is not supported")

    def display(self):
        self.cap.display()

    def get(self):
        """ return latest frame """
        return self.cap.get()

    def run(self):
        """ start and run a thread for grabbing frames from capture """
        return self.cap.run()

    def stop(self):
        """ stops video capture """
        self.cap.stop()

    def update(self):
        """ update frame from capture """
        self.cap.update()
