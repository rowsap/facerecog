import cv2
import numpy as np
import os
import logging as log
from time import sleep
import datetime as dt

def readCam(faceRecognizer):
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontscale = 1
    fontcolor = (255, 255, 255)

    # Use the Project Cascade XML created on the previous step
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    print(faceCascade)
    # Open the Camera for reading
    cam = cv2.VideoCapture(0);
    anterior = 0
    # Display all the logging information to the project Log
    log.basicConfig(filename='webcam.log', level=log.INFO)

    id = 0
    while (True):
        if not cam.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass
        ret, img = cam.read();
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        cv2.imshow("Face", img);
        if (cv2.waitKey(1) == ord('q')):
            break;
        # read through all the faces in the screen frame
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, conf = faceRecognizer.predict(gray[y:y + h, x:x + w])

            if (id == 1):
                id = "Ayana";
            elif (id == 2):
                id = "Saptarshi";
            else:
                id = "Not Known";
            print(id)
            print(conf)
            cv2.putText(img, str(id), (x, y - 10), font, 0.55, (0, 255, 0), 1);

            if (conf <= 20):
                if (id != None):
                    cv2.putText(img, str(id), (x, y - 10), font, 0.55, (0, 255, 0), 1);
            else:
                cv2.putText(img, "Unknown", (x, y + h - 10), font, 0.55, (0, 255, 0), 1);
            if anterior != len(faces):
                anterior = len(faces)
                log.info("ID: " + str(id) + " faces: " + str(len(faces)) + " at " + str(dt.datetime.now()))

    cam.release()
    cv2.destroyAllWindows()

def chkIndivPic(srcFile,faceRecognizer):
    image = cv2.imread(srcFile)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    user, confidence = faceRecognizer.predict(image)
    print(user)
    print(confidence)
