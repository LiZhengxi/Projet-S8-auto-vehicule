# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import serial
def detection(image):
    #transform the image from format BGR to HSV
	HSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	#set the scope of the color red in HSV
	lower_red = np.array([160,123,0])
	upper_red = np.array([179,255,255])
	#cut down the red part
	mask = cv2.inRange(HSV,lower_red,upper_red)
	dilated = cv2.dilate(mask,cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)),iterations=1)
	contours, hierarchy = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	if contours:
            areaMax = 0
             #check every red contours in this image
            for i in range(len(contours)) :
                area = cv2.contourArea(contours[i])
                if(area>=areaMax) :
                    j=i
                    areaMax=area
            if areaMax>400:
                    #exclude the disturbs according to the surface of the contour
                x,y,w,h = cv2.boundingRect(contours[j])
                    #cut down the red part of the image
                cro = image[y:y+h,x:x+w]
                im_gray1 = cv2.cvtColor(cro,cv2.COLOR_BGR2GRAY)
                    # function threshold : the third parametre 151 means level gray less than 255 convert in black the orther white
                retval,im_at_fixed1= cv2.threshold(im_gray1,250,255,cv2.THRESH_BINARY)
                value = im_at_fixed1[::2]
                average = cv2.mean(value)
                print(average)
                if(average[0]<=3) :
                    print("Panneau stop")
                    info = 'p'
                else :
                    print("Feu rouge")
                if(cro is not None) :
                    cv2.imshow("test",cro)
            else :
                print("notting")
                info ='z'
        else :
            print("notting here ")
            info = 'z'
        return info
def detection_green(image) :
    #transform the image from format BGR to HSV
	HSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	#set the scope of the color red in HSV
	lower_green = np.array([35,43,0])
        upper_green = np.array([77,255,255])
	#cut down the red part
	mask1 = cv2.inRange(HSV,lower_green,upper_green)
        dilated1 = cv2.dilate(mask1,cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)),iterations=1)
        contours, hierarchy = cv2.findContours(dilated1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	if contours:
            areaMax = 0
             #check every red contours in this image
            for i in range(len(contours)) :
                area = cv2.contourArea(contours[i])
                if(area>=areaMax) :
                    j=i
                    areaMax=area
            if areaMax>300:
                    #exclude the disturbs according to the surface of the contour
                x,y,w,h = cv2.boundingRect(contours[j])
                    #cut down the red part of the image
                cro = image[y:y+h,x:x+w]
                im_gray1 = cv2.cvtColor(cro,cv2.COLOR_BGR2GRAY)
                    # function threshold : the third parametre 151 means level gray less than 255 convert in black the orther white
                retval,im_at_fixed1= cv2.threshold(im_gray1,250,255,cv2.THRESH_BINARY)
                value = im_at_fixed1[::2]
                average = cv2.mean(value)
                print(average)
                if(average[0]==0) :
                    print("Feu vert eteind")
                    info = 'f'
                else :
                    print("Feu vert allume")
                    info ='o'
                    
                if cro is not None :
                    cv2.imshow("test",cro)
            else :
                print("not feu vert")
                info ='i'
        return info
    

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (480, 320)
camera.framerate = 32
camera.hflip = False
camera.vflip = True
rawCapture = PiRGBArray(camera, size=(480, 320))
ser = serial.Serial('/dev/ttyACM0',115200)
# allow the camera to warmup
time.sleep(2)
info1 ='z'
# capture frames from the camera
#3 windows video original,video gray, video black-white
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
        info=detection(image)
        cv2.imshow("original",image)
        
        # size 640x480 =307200
        #print(im_at_fixed.size)
        # shape
        #print(im_at_fixed.shape)
        #print(im_at_fixed.dtype)
        if(info1=='f'):
            info=detection_green(image)
            if(info=='o'):
                info='z'
        ser.write(info)
        info1=info
	# show the frame
	key = cv2.waitKey(1) & 0xFF
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
ser.write('i')

