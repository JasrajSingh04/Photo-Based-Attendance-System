from ast import Return
from copy import deepcopy
import datetime
import imp
from re import I
import cv2
import glob
import io

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

rows = run_query("SELECT * from student_ca")

clean_db=pd.DataFrame(rows,columns=["Roll no","Name","Prac"])


st.dataframe(clean_db)

with st.form(key="query_form",clear_on_submit=True):
    input_rno=st.number_input("Enter Roll No",min_value=1, max_value=50, step=1)
    input_sname=st.text_input("Enter Student Name")
    image_File = st.file_uploader(label = "Upload file", type=["jpg","png"])
    submit_code=st.form_submit_button("Execute")




if submit_code:
    get_image_name=run_query(f"select * from student_ca where photo_link like \"D:/3rd Year Project/3rd-year-project/Connecting SQL/SQL FILES IMAGES/{image_File.name}\"")
    get_roll_no=run_query(f"select * from student_ca where RollNo like {input_rno}")
    get_sname=run_query(f"select * from student_ca where StudentName like \"{input_sname}\"")
    if get_roll_no:
        st.error(f"{input_rno} already exists")
    elif get_sname:
        st.error(f"{input_sname} already exists")
    elif get_image_name:
        st.error(f"{image_File.name} already exists")
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
    global newdir_lock
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
    print("done saving")



with st.form(key="Get_Attendence",clear_on_submit=True):
    attendence_file = st.file_uploader(label = "Upload file", type=["jpg","png"])
    submit_attendence=st.form_submit_button("Get Attendence")
    



if attendence_file is not None:
    faces()
    st.success("done saving")
    photo_data=run_query("select photo_link from student_ca")
    for data in photo_data:
        image_link=data[0]
        for img in glob.glob("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock+"/*.jpg"):
            ImageOfAttendece=cv2.imread(img)
            ImageOfDatabase=cv2.imread(image_link)
            resultmain=DeepFace.verify(ImageOfAttendece,ImageOfDatabase,model_name="Facenet", enforce_detection=False,detector_backend="mtcnn")
            print(resultmain)
            print(image_link)
            print(img)



