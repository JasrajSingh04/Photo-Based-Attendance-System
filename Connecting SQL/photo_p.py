from ast import Import
import base64
import glob

import io

from turtle import heading
import mysql.connector
from dis import Instruction
from re import MULTILINE
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter
import pandas as pd
from xml.etree.ElementTree import Comment
import cv2
import os
import dlib
from tkinter.filedialog import askdirectory
from pip import main
from deepface import DeepFace
from pyparsing import col


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jasrajsql",
  database="testdb"
)

cursor=mydb.cursor()

query = 'select * from student_ca'
  
# Execute the query to get the file
cursor.execute(query)
  
data = cursor.fetchall()



# for x in data:
#     image_link=x[0]
#     for img in glob.glob("F:\\VS code python\\Python face-recognition try\\test_faces\\*.jpg"):
#           per_image_1=cv2.imread(img)
#           image=cv2.imread(image_link)
#           resultmain=DeepFace.verify(per_image_1,image,model_name="Facenet", enforce_detection=False,detector_backend="mtcnn")
#           print(resultmain)
#           print(image_link)
#           print(img)

sql_query = pd.read_sql_query('''
                              select * from student_ca
                              '''
                              ,mydb)
df = pd.DataFrame(sql_query)
df.to_csv (r'F:\VS code python\Python face-recognition try\df.csv', index = False) # place 'r' before the path name
print("done saving")