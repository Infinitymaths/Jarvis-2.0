# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 11:58:21 2021

@author: SHARATH
"""

import cv2
import numpy as np
from PIL import Image
import os

path = 'samples'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def Images_And_Labels(paths):
    imagepath = [os.path.join(paths,f) for f in os.listdir(paths)]
    faceSamples = []
    ids = []
    
    for imagePath in imagepath:
        gray_img = Image.open(imagePath).convert('L')
        img_arr = np.array(gray_img,'uint8')
        
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_arr)
        
        for(x,y,w,h) in faces:
            faceSamples.append(img_arr[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids

print("Training the faces.. please wait")
faces,ids = Images_And_Labels(path)
recognizer.train(faces,np.array(ids))

recognizer.write("trainer/trainer.yml")

print("model is trained and ready for action...")