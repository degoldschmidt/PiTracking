# import the necessary packages
from __future__ import print_function
from imutils.video import VideoStream
import argparse
import imutils
import cv2
import time

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--numframes", type=int, default=100,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=1,
	help="Whether or not frames should be displayed")
ap.add_argument("-fps", "--framespersec", type=int, default=25,
	help="Target FPS")
args = vars(ap.parse_args())

# loop over some frames
print("Capturing {0} frames".format(args["numframes"]))
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FPS, args["framespersec"])

# created a *threaded *video stream, allow the camera senor to warmup,
# and start the FPS counter
#print("[INFO] sampling THREADED frames from RPiCam...")
#vs = VideoStream(src=0).start()

# loop over some frames...this time using the threaded stream
counter = 0
 # Start time
start = time.time()
while counter < args["numframes"]:
	# grab the frame from the stream and resize it to have a maximum
	# width of 400 pixels
	(grabbed, frame) = capture.read()

	# check to see if the frame should be displayed to our screen
	if args["display"] > 0:
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
        counter += 1

# End time
end = time.time()

# Time elapsed
seconds = end - start
print("Time taken : {0} seconds".format(seconds))

# Calculate frames per second
fps  = args["numframes"] / seconds
print("Estimated frames per second : {0}".format(fps))
# do a bit of cleanup
capture.release()
cv2.destroyAllWindows()
