"""
ESIGELEC Projet S8
Programme de Traitement d'image
Detection de Panneau Stop et Feux de Signalisations
Dupin Esther
Ponapin Brian
Groupe A1
Enseignant : Yann Duchemin
"""
#Importation des librairies necessaires

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import matplotlib

#Parametres camera

camera=PiCamera()#Activation de la caméra
camera.resolution = (512,304)#Resolution de la picaméra
camera.framerate = 60#Nombre d'image par seconde
rawCapture = PiRGBArray(camera,size = (512,304))

#Boucle infini permettant d'avoir plusieurs images pour avoir la video 
for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
    ordre='av'#Variable permettant de donner un ordre au robot
    image = frame.array#Stockage de l'image actuelle dans une variable image
    key = cv2.waitKey(1) & 0xFF#Permet d'avoir le flux video en direct
    rawCapture.truncate(0)#Nettoie le flux vidéo pour la prochaine fenetre

    
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#Permet de convertir une image couleur en gris

    template = cv2.imread('stop.png',0)#Permet d'importer la photo du panneau stop
    w , h = template.shape[::-1]#Recupere les données de la photo panneau stop
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5#Pourcentage entre l'image d'origine et l'objet utilisé dans la video
    loc = np.where(res >= threshold)
    
    #Condition if permettant de detecter le panneau stop
    if np.any(res>=threshold):
        #Variable permettant de donner un ordre au robot
        ordre='s'
        
        #Boucle for permettant d'afficher un rectangle bleu lors de la detection du panneau stop
        for pt in zip(*loc[::-1]):
            cv2.rectangle(image,pt, (pt[0]+w,pt[1]+h),(255,0,0),2)

    template2 = cv2.imread('feuxrougerogner1.jpg',0)#Permet d'importer la photo des feux de signalisations
    w2 , h2 = template2.shape[::-1]#Recupere les données de la photo feux de signalisation
    res2 = cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
    threshold2 = 0.75#Pourcentage entre l'image d'origine et l'objet utilisé dans la video
    loc2 = np.where(res2 >= threshold2)
    
     #Condition if permettant de detecter les feux de signalisations
    if np.any(res2>=threshold2):
        #Variable permettant de donner un ordre au robot
        ordre='fr'
        
        #Boucle for permettant d'afficher un rectangle rouge lors de la detection du feux
        for pt in zip(*loc2[::-1]):
            cv2.rectangle(image,pt, (pt[0]+w2,pt[1]+h2),(0,0,255),2)

    print(ordre)#Affichage du robot   
    cv2.imshow('Direct',image)#Affichage de l'image dans la fenetre direct
