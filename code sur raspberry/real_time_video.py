# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	img = frame.array
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #Blur image to reduce noise
	blurred = cv2.GaussianBlur(gray, (9, 9), 0)

        #Perform canny edge-detection
	edged = cv2.Canny(blurred, 50, 150)

        #Perform hough lines probalistic transform
	lines = cv2.HoughLinesP(edged,1,np.pi/180,10,80,1)

        #Draw lines on input image
	if(lines != None):
		for x1,y1,x2,y2 in lines[0]:
			cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
	# show the frame
	cv2.imshow("Frame", img)
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break