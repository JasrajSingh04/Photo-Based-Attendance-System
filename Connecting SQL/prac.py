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


st.title("hello")


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jasrajsql",
  database="testdb"
)

myc=mydb.cursor()


@st.experimental_memo(ttl=10)
def run_query(query):
    with mydb.cursor() as cur:
        cur.execute(query)
        data= cur.fetchall()
        mydb.commit()
        return data

def load_image(image_File):
    img=Image.open(image_File)
    return img



# clean_db=pd.DataFrame(rows,columns=["Roll no","Name","Prac"])


with st.form(key="query_form",clear_on_submit=True):
    input_rno=st.number_input("Enter Roll No",step=1)
    input_sname=st.text_input("Enter Student Name")
    image_File = st.file_uploader(label = "Upload file", type=["jpg","png"])
    submit_code=st.form_submit_button("Execute")


try:
    if submit_code:
        
        
        get_image_name=run_query(f"select * from student_ca where photo_link like \"D:/3rd Year Project/3rd-year-project/Connecting SQL/SQL FILES IMAGES/{image_File.name}\"")
        get_roll_no=run_query(f"select * from student_ca where RollNo like {input_rno}")
        get_sname=run_query(f"select * from student_ca where StudentName like \"{input_sname}\"")
        if get_roll_no:
            st.error(f"Roll no {input_rno} already exists")
        elif get_sname:
            st.error(f"Student name {input_sname} already exists")
        elif get_image_name:
            st.error(f"Image {image_File.name} already exist.Use a different Image name ")
        else:
            imageface=face_recognition.load_image_file(image_File)
            faceloc=face_recognition.face_locations(imageface)
            if faceloc:
                with open(os.path.join("D:\\3rd Year Project\\3rd-year-project\\Connecting SQL\\SQL FILES IMAGES",image_File.name),"wb") as f:
                    f.write(image_File.getbuffer())
                run_query(f"INSERT into student_CA(rollno,StudentName,photo_link) VALUES({input_rno},\"{input_sname}\",\"D:/3rd Year Project/3rd-year-project/Connecting SQL/SQL FILES IMAGES/{image_File.name}\")")
                st.success("Submitted")
            else:
                st.error("Face is required in image")
except:
    st.error("Fill all the Columns")



















    

    
            







