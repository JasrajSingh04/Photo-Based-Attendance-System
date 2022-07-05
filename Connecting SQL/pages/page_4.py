
from ast import Return
from copy import deepcopy
import datetime
import imp

from re import I
from tkinter import Frame
import cv2
import glob
import io
import pyodbc
from deepface import DeepFace
from turtle import clear
from matplotlib import image
from mysqlx import Column
import numpy as np
import streamlit as st
import mysql.connector
import dlib
import pandas as pd
from PIL import Image,ImageEnhance
import os
from PIL import Image , ImageOps , ImageDraw , ImageFont
from typer import Exit
import face_recognition
from prac import *
from pages.page_2 import *









# def MyRec(rgb,x,y,w,h,v=20,color=(200,0,0),thikness =200):
#     """To draw stylish rectangle around the objects"""
#     cv2.line(rgb, (x,y),(x+v,y), color, thikness)
#     cv2.line(rgb, (x,y),(x,y+v), color, thikness)

#     cv2.line(rgb, (x+w,y),(x+w-v,y), color, thikness)
#     cv2.line(rgb, (x+w,y),(x+w,y+v), color, thikness)

#     cv2.line(rgb, (x,y+h),(x,y+h-v), color, thikness)
#     cv2.line(rgb, (x,y+h),(x+v,y+h), color, thikness)

#     cv2.line(rgb, (x+w,y+h),(x+w,y+h-v), color, thikness)
#     cv2.line(rgb, (x+w,y+h),(x+w-v,y+h), color, thikness)

# def save(img,name, bbox, width=180,height=227):
#     x, y, w, h = bbox
#     imgCrop = img[y:h, x: w]
#     imgCrop = cv2.resize(imgCrop, (width, height))#we need this line to reshape the images
#     cv2.imwrite(name+".jpg", imgCrop)

# def faces():
#     global newdir_lock
#     global new_path
#     newdir=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#     newdir_lock=newdir
#     os.mkdir("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/" + newdir)
    
#     detector = dlib.get_frontal_face_detector()
#     new_path ="D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock+"/Image_"
#     file_bytes = np.asarray(bytearray(attendence_file.read()), dtype=np.uint8)
#     opencv_image = cv2.imdecode(file_bytes, 1)  
#     frame =opencv_image
#     gray = frame
#     faces = detector(gray)
#     fit =20
#     # detect the face
#     for counter,face in enumerate(faces):
#         print(counter)
#         x1, y1 = face.left(), face.top()
#         x2, y2 = face.right(), face.bottom()
#         cv2.rectangle(frame,(x1,y1),(x2,y2),(220,255,220),1)
#         MyRec(frame, x1, y1, x2 - x1, y2 - y1, 10, (0,250,0), 3)
#         # save(gray,new_path+str(counter),(x1-fit,y1-fit,x2+fit,y2+fit))
#         save(gray,new_path+str(counter),(x1,y1,x2,y2))
#     frame = cv2.resize(frame,(800,800))
#     cv2.imshow("im1",frame) 
#     cv2.waitKey(0)  
#     print("done saving")


# lecture_name=run_query("Select * from lnames")
# lname=[]
# for lecture in lecture_name:
#     lnamefor=lecture[0]
#     lname.append(lnamefor)




# with st.form(key="GetAttendence",clear_on_submit=True):
    
#     date=st.date_input("Select Attendence Date",datetime.date.today())
#     col1, col2 = st.columns([1,1])
#     with col1:
#         start_time=st.time_input("From")
#     with col2:
#         end_time=st.time_input("To")
#     lecture = st.selectbox("Lecture",lname)
#     attendence_file = st.file_uploader(label = "Upload file", type=["jpg","png","jfif"])
#     submit_attendence=st.form_submit_button("Attendence")
    











# if attendence_file is not None:
#     faces()
#     st.success("done saving")
#     time = datetime.datetime.now().strftime('%Y-%m-%d')
#     locktime=time
#     run_query(f"alter table student_ca ADD COLUMN `{locktime}` varchar(255);")
#     photo_data=run_query("select photo_link from student_ca")
#     for data in photo_data:
#         image_link=data[0]
#         for img in glob.glob("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock+"/*.jpg"):
#             ImageOfAttendece=cv2.imread(img)
#             ImageOfDatabase=cv2.imread(image_link)
#             resultmain=DeepFace.verify(ImageOfAttendece,ImageOfDatabase,model_name="Facenet", enforce_detection=False,detector_backend="mtcnn")
#             if resultmain["verified"] is True:
#                 run_query(f"update student_ca set `{locktime}` = \"present\" where photo_link=\"{image_link}\" ")
#                 break 
#     print("completed loop")
#     run_query(f"UPDATE student_ca  SET `{locktime}`=COALESCE(`{locktime}`,\"absent\");")
#     sql_query = pd.read_sql_query('''
#                               select * from student_ca
#                               '''
#                               ,mydb)
#     df=pd.DataFrame(sql_query)
#     df.to_csv(fr"{new_path}+{locktime}+.csv",index=False)
#     print("done")
#     run_query(f"alter table student_ca drop column `{locktime}`")
