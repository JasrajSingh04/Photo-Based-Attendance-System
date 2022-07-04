from dis import Instruction
from re import MULTILINE
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter
from xml.etree.ElementTree import Comment
import cv2
import os
import dlib
from tkinter.filedialog import askdirectory




detector = dlib.get_frontal_face_detector()
new_path = "F:/VS code python/Python face-recognition try/tf2/tf_1_"

def MyRec(rgb,x,y,w,h,v=20,color=(200,0,0),thikness =200):
    """To draw stylish rectangle around the objects"""
    cv2.line(rgb, (x,y),(x+v,y), color, thikness)
    cv2.line(rgb, (x,y),(x,y+v), color, thikness)

    cv2.line(rgb, (x+w,y),(x+w-v,y), color, thikness)
    cv2.line(rgb, (x+w,y),(x+w,y+v), color, thikness)

    cv2.line(rgb, (x,y+h),(x,y+h-v), color, thikness)
    cv2.line(rgb, (x,y+h),(x+v,y+h), color, thikness)

    cv2.line(rgb, (x+w,y+h),(x+w,y+h-v), color, thikness)
    cv2.line(rgb, (x+w,y+h),(x+w-v,y+h), color, thikness)

def save(img,name, bbox, width=180,height=227):
    x, y, w, h = bbox
    imgCrop = img[y:h, x: w]
    imgCrop = cv2.resize(imgCrop, (width, height))#we need this line to reshape the images
    cv2.imwrite(name+".jpg", imgCrop)

def faces():
    frame =cv2.imread("F:/VS code python/Python face-recognition try/Photos/T3.jpg")
    gray = frame
    faces = detector(gray)
    fit =20
    # detect the face
    for counter,face in enumerate(faces):
        print(counter)
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()
        cv2.rectangle(frame,(x1,y1),(x2,y2),(220,255,220),1)
        MyRec(frame, x1, y1, x2 - x1, y2 - y1, 10, (0,250,0), 3)
        # save(gray,new_path+str(counter),(x1-fit,y1-fit,x2+fit,y2+fit))
        save(gray,new_path+str(counter),(x1,y1,x2,y2))
    frame = cv2.resize(frame,(800,800))
    cv2.imshow('img',frame)
    cv2.waitKey(0)
    print("done saving")
faces()



