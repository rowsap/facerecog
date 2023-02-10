# This is a sample Python script.
import cv2
import os

from getAllFaces import getAllFaces
from trainmodel import *
from faceRecog import *


images = [] #use for image data
labels = [] #use for image label data
faceRecognizer = cv2.face.LBPHFaceRecognizer_create()

def process():
    # Download all the Faces
    getAllFaces ("C:\\Users\\rowsa\\Documents\\imgSort", "C:\\projects\\imgtrain\\faces" )

    #Need set of individual photos for each of the persons you need face recogition for
    #Alternatively, manually select the photes from the above destination folder and into individual folders
    trainmodel ("C:\\projects\\imgtrain\\ayana",1,faceRecognizer)
    trainmodel ("C:\\projects\\imgtrain\\sap",2,faceRecognizer)
    dlCascade(faceRecognizer)
    readCam(faceRecognizer)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    process()
