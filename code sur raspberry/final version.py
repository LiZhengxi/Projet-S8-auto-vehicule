'''
		Name: raspberry autocar
		Autheur : LiZhengxi
		Date : 2018.04.25
		Comment :  this programme can recognize the white line, the red light and the street nameplate
				   when the car see the red light it will stop and wait for the green lignt appear.
				   if the car see the street nameplate, it will stop and wait for 2.5s
				   if notting here, it will follow the white line
'''

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import serial
'''
in this part check the red light and the street nameplate
use the method recognize the color then according to the brightness to distinguish the red light and street nameplate
'''
def detection(image):
    #transform the image from format BGR to HSV
	HSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	#set the scope of the color red in HSV
	lower_red = np.array([160,123,0])
	upper_red = np.array([179,255,255])
	#recognize the red part
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
                # function threshold : the third parametre 250 means level gray less than 255 convert in black the orther white
                retval,im_at_fixed1= cv2.threshold(im_gray1,250,255,cv2.THRESH_BINARY)
				# cherck the brightness of this image
                value = im_at_fixed1[::2]
                average = cv2.mean(value)
                print(average)
                if(average[0]==0) :
                    print("Panneau stop")
					#waiting for 2.5s and then go ahead
                    ser.write('s')
                    time.sleep(2.5)
                    ser.write('z')
                    time.sleep(0.75)
                    ser.write('d')
                    info = 'p'
                else :
                    print("Feu rouge")
                    info='f'
                
                if(cro is not None) :
                    cv2.imshow("test",cro)
            else :
                print("notting")
                info ='z'
        else :
            print("notting here ")
            info = 'z'
        return info
'''
the same method to recognize the green part
''' 
def detection_green(image) :
    #transform the image from format BGR to HSV
	HSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	#set the scope of the color green in HSV
	lower_green = np.array([35,43,0])
        upper_green = np.array([77,255,255])
	#recognize the green part
	mask1 = cv2.inRange(HSV,lower_green,upper_green)
        dilated1 = cv2.dilate(mask1,cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)),iterations=1)
        contours, hierarchy = cv2.findContours(dilated1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	if contours:
            areaMax = 0
             #check every green contours in this image
            for i in range(len(contours)) :
                area = cv2.contourArea(contours[i])
                if(area>=areaMax) :
                    j=i
                    areaMax=area
            if areaMax>300:
                #exclude the disturbs according to the surface of the contour
                x,y,w,h = cv2.boundingRect(contours[j])
                #cut down the green part of the image
                cro = image[y:y+h,x:x+w]
                im_gray1 = cv2.cvtColor(cro,cv2.COLOR_BGR2GRAY)
                # function threshold : the third parametre 250 means level gray less than 255 convert in black the orther white
                retval,im_at_fixed1= cv2.threshold(im_gray1,250,255,cv2.THRESH_BINARY)
                # cherck the brightness of this image
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
        else :
            info='i'
        
        return info
    

# initialize the camera and grab a reference to the raw camera capture and the communication serial
camera = PiCamera()
camera.resolution = (480, 320)
camera.framerate = 32
camera.hflip = False
camera.vflip = True
rawCapture = PiRGBArray(camera, size=(480, 320))
#set the baud rate :250000
ser = serial.Serial('/dev/ttyACM0',250000)
# allow the camera to warmup
time.sleep(2)
#initialize the different barycenter
c1=0
c2=0
c3=0
cx=0
cy=0
info1='z'
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
	#every time check the red light and the street nameplate
    info=detection(image)
	#if red light stop the car
    if(info=='f'):
        ser.write('i')
	#if the last frame is red light and this frame is green light start the motor
    if(info1=='f') :
            info=detection_green(image)
            if(info=='o') :
                info='z'
            else :
                ser.write('m') 
	#if no red light no strret nameplate follow the line	
    if(info=='z'):
            croq = image[160:320,0:480]
            im_gray = cv2.cvtColor(croq,cv2.COLOR_BGR2GRAY)
            # function threshold : the third parametre 220 means level gray less than 255 convert in black the orther white
            retval,im_at_fixed = cv2.threshold(im_gray,220,255,cv2.THRESH_BINARY)
            cv2.imshow("black",im_at_fixed)
            cv2.imshow("gray",im_gray)
            contours1, hierarchy = cv2.findContours(im_at_fixed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            #find the contours area
            area1 = 0
            for i in range(len(contours1)) :
                area = cv2.contourArea(contours1[i])
                if area >2000 :
                    M=cv2.moments(contours1[i])
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    cv2.drawContours(croq,contours1[i],-1,(0,255,0),2)
                    print(cx,cy)
		    #record the barycenter in this moment and the 2 previous moments
            c3=c2
            c2=c1
            c1=cx
            cv2.circle(croq,(c1,cy),5,(0,0,255),5)
            cv2.circle(croq,(c2,cy),5,(0,255,0),5)
            cv2.circle(croq,(c3,cy),5,(255,0,0),5)
			#according to those barycenter to do different move
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
                cv2.imshow("line",croq)
        info1=info
		# show the frame
        cv2.imshow("original",image)
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
ser.write('i')
