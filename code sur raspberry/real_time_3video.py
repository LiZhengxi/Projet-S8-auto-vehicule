# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (240, 128)
camera.framerate = 32
camera.hflip = False
camera.vflip = True
rawCapture = PiRGBArray(camera, size=(240, 128))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
#3 windows video original,video gray, video black-white
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
	im_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	# function threshold : the third parametre 5 means level gray less than 5 convert in black the orther white
        retval,im_at_fixed = cv2.threshold(im_gray,5,255,cv2.THRESH_BINARY)
        cv2.imshow("black",im_at_fixed)
        
    
        # size 640x480 =307200
        #print(im_at_fixed.size)
        # shape
        #print(im_at_fixed.shape)
        #print(im_at_fixed.dtype)
        resl = 0
        resr = 0
        for i in range(128):
            for j in range(120):
                    if im_at_fixed[i,j]==0:
                        if j<64 :
                            resl=resl+1
                        else :
                            resr=resr+1
                            
        print (resl)
        print (resr)
        print("\n")
	# show the frame
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break