import datetime
from dis import Instruction
import glob
from re import MULTILINE
from tkinter import *
from PIL import Image
import streamlit as st
import tkinter
import numpy as np
import cv2
import os
import dlib


def MyRec(rgb,x,y,w,h,v=20,color=(200,0,0),thikness =2):
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
    global newdir_lock
    global new_path
    newdir=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    newdir_lock=newdir
    os.mkdir("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/" + newdir)
    
    detector = dlib.get_frontal_face_detector()
    new_path ="D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock+"/Image_"
    file_bytes = np.asarray(bytearray(attendence_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)  
    frame =opencv_image
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
    cv2.imwrite("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock+"/Mainpicture.jpg",frame)


with st.form(key="getstandard",clear_on_submit=False):
    attendence_file = st.file_uploader(label = "Upload file", type=["jpg","png","jfif"],accept_multiple_files=True)
    submit_btn_for_form=st.form_submit_button()

if submit_btn_for_form:
    for counter,uploaded_file in enumerate(attendence_file):
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        frame = opencv_image  
        cv2.imwrite("D:/3rd Year Project/3rd-year-project/Connecting SQL/Test Files/images/im_name"+str(counter)+".jpg",frame)

    
    for img in glob.glob("D:/3rd Year Project/3rd-year-project/Connecting SQL/Test Files/images/*.jpg"):
        img1=Image.open(img)
        st.image(img1)
     

