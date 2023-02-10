import cv2
import os

def getAllFaces(srcDir,destDir):
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    i = 0
    for files in os.listdir(srcDir):
        if ".jpg" in files:
            image = cv2.imread(os.path.join(srcDir,files))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            for (x, y, w, h) in faces:
                thumbnail = image[y:y + h, x:x + w]
                i = i + 1
                filename = os.path.join(destDir,str(i) + ".jpg")
                cv2.imwrite(filename,thumbnail)