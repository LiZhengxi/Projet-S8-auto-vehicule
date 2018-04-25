# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import serial
import time
ser = serial.Serial('/dev/ttyACM0',115200)
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (480, 320)
camera.framerate = 32
camera.hflip = False
camera.vflip = True
rawCapture = PiRGBArray(camera, size=(480, 320))

# allow the camera to warmup et initiasize the communication serial
time.sleep(2)
 
c1=0
c2=0
c3=0
cx=0
cy=0
# capture frames from the camera
#3 windows video original,video gray, video black-white
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
	cro = image[160:320,0:480]
	im_gray = cv2.cvtColor(cro,cv2.COLOR_BGR2GRAY)
	# function threshold : the third parametre 151 means level gray less than 255 convert in black the orther white
        retval,im_at_fixed = cv2.threshold(im_gray,220,255,cv2.THRESH_BINARY)
        cv2.imshow("black",im_at_fixed)
        cv2.imshow("gray",im_gray)
        contours, hierarchy = cv2.findContours(im_at_fixed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #cherche la surface des contours
        area = 0
        for i in range(len(contours)) :
            area = cv2.contourArea(contours[i])
            if area >2000 :
                M=cv2.moments(contours[i])
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.drawContours(cro,contours[i],-1,(0,255,0),2)
                print(cx,cy)
        c3=c2
        c2=c1
        c1=cx
        cv2.circle(cro,(c1,cy),5,(0,0,255),5)
        cv2.circle(cro,(c2,cy),5,(0,255,0),5)
        cv2.circle(cro,(c3,cy),5,(255,0,0),5)
        if(abs(c1-c2)<=5&abs(c2-c3)<=5):
            ser.write('z')
       
        else :
            
            if(c1<c2):
                if(c2<c3):
                    ser.write('d')
            elif(c1>c2):
                if(c2>c3):
                    ser.write('q')
            else :
                ser.write('z')
        cv2.imshow("frame",image)
        # size 640x480 =307200
        #print(im_at_fixed.size)
        # shape
        #print(im_at_fixed.shape)
        #print(im_at_fixed.dtype)
        
	# show the frame
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
ser.write('i')