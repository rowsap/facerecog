import cv2
import numpy as np
import os
import logging as log
from time import sleep
import datetime as dt

def trainmodel(srcDir,user,faceRecognizer):
    #cascPath = "C:\\Users\\rowsa\\Documents\\Pictures\\0409\\haarcascade_frontalface_default.xml"
    #faceCascade = cv2.CascadeClassifier(cascPath)    
    i = 0
    print ("trainmodel")
    images = []
    labels = []
    for files in os.listdir(srcDir):
        if ".jpg" in files:
            image = cv2.imread (os.path.join(srcDir,files))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            images.append(image)
            labels.append(user)
    faceRecognizer.train(images,np.array(labels))

def dlCascade(faceRecognizer):
    faceRecognizer.save("projectCascade.xml")
