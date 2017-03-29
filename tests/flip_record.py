import numpy as np
import cv2
import time
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--numframes", type=int, default=100,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=1,
	help="Whether or not frames should be displayed")
ap.add_argument("-fps", "--framespersec", type=int, default=25,
	help="Target FPS")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(0)

# Define codec and VideoWriter object
out = cv2.VideoWriter("output_nodis.avi", cv2.VideoWriter_fourcc(*'DIVX'), 20.0, (640,480))

start = time.time()
counter = 0
while counter < args["numframes"]:
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)

        # write flipped frame
        out.write(frame)

        #cv2.imshow("frame", frame)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break
        counter += 1
    else:
        break

# End time
end = time.time()

# Time elapsed
seconds = end - start
print("Time taken : {0} seconds".format(seconds))

# Calculate frames per second
fps  = args["numframes"] / seconds
print("Estimated frames per second : {0}".format(fps))

# finally, release all
cap.release()
out.release()
cv2.destroyAllWindows()
