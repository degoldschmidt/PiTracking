# import the necessary packages
from __future__ import print_function
from imutils.video import VideoStream
import argparse
import imutils
import cv2
import time

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=1,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

# grab a pointer to the video stream and initialize the FPS counter
stream = cv2.VideoCapture(0)
# Find OpenCV version
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

# With webcam get(CV_CAP_PROP_FPS) does not work.
# Let's see for ourselves.
if int(major_ver)  < 3 :
	fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
	print "Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps)
else :
	fps = video.get(cv2.CAP_PROP_FPS)
    print "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps)

# loop over some frames
print "Capturing {0} frames".format(args["num_frames"])
 # Start time
start = time.time()
while fps._numFrames < args["num_frames"]:
	# grab the frame from the stream and resize it to have a maximum
	# width of 400 pixels
	(grabbed, frame) = stream.read()
	#frame = imutils.resize(frame, width=400)

	# check to see if the frame should be displayed to our screen
	if args["display"] > 0:
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

# End time
end = time.time()

# Time elapsed
seconds = end - start
print "Time taken : {0} seconds".format(seconds)

# Calculate frames per second
fps  = num_frames / seconds;
print "Estimated frames per second : {0}".format(fps);
# do a bit of cleanup
stream.release()
cv2.destroyAllWindows()

# created a *threaded *video stream, allow the camera senor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from webcam...")
vs = VideoStream(src=0).start()

# loop over some frames...this time using the threaded stream
while fps._numFrames < args["num_frames"]:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	#frame = imutils.resize(frame, width=400)

	# check to see if the frame should be displayed to our screen
	if args["display"] > 0:
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
