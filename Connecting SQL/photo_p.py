from ast import Import
import base64
import glob

import io
from random import random
import re
import re
from turtle import heading
from cv2 import dft
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
import datetime
from tkinter.filedialog import askdirectory
from pip import main
from deepface import DeepFace
from pyparsing import Or, col
from datetime import datetime

from scipy import rand

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jasrajsql",
  database="testdb"
)

cursor=mydb.cursor()

standard_sel="FYIT"

  

query = f'''
select  timetable_data.tt_fromtime, timetable_data.tt_totime from timetable_data inner join teacher_data on timetable_data.tt_lecturename=teacher_data.teacherid
 where timetable_data.tt_standard=\"FYIT\" and teacher_data.teacherlecture like \"MATHS 1\" and teacher_data.teachername like \"malika kaur\" and timetable_Data.tt_Dayofweek like \"monday\"
'''

cursor.execute(query)
  
data = cursor.fetchall()


lecture="MATHS G4 AND G5                  sd"

print(lecture)

FullNameOfStudent=re.sub(' +', ' ',lecture)
print(FullNameOfStudent)


# timelist=[]

# for time in data:

#   x=time[0]

#   y=time[1]

#   listoftimes=x+" to "+y
#   timelist.append(listoftimes)
  


# randomvar=timelist[0]

# print(randomvar)

# x=randomvar.split(" to ")

# print(x[0] , x[1])




# for url in data:
#   print(url[0])
#   os.remove(url[0])



# print(data)

# for l in data:
#   print(l[0]+" "+l[1]+" "+l[2])




















# Execute the query to get the file




# for x in data:
#     image_link=x[0]
#     for img in glob.glob("F:\\VS code python\\Python face-recognition try\\test_faces\\*.jpg"):
#           per_image_1=cv2.imread(img)
#           image=cv2.imread(image_link)
#           resultmain=DeepFace.verify(per_image_1,image,model_name="Facenet", enforce_detection=False,detector_backend="mtcnn")
#           print(resultmain)
#           print(image_link)
#           print(img)

# sql_query = pd.read_sql_query('''
#                               select * from student_ca
#                               '''
#                               ,mydb)
# df = pd.DataFrame(sql_query)
# df.to_csv (r'F:\VS code python\Python face-recognition try\df.csv', index = False) # place 'r' before the path name
# print("done saving")


































# time_fromdt="08:55:00"
# time_todt="09:25:00"

# time_fromdt_tot=datetime.strptime(time_fromdt, '%H:%M:%S').time()
# time_todt_tot=datetime.strptime(time_todt, '%H:%M:%S').time()


# for time in data:
#   time0=datetime.strptime(time[0], '%H:%M:%S').time()
#   time1=datetime.strptime(time[1], '%H:%M:%S').time()

#   if (time0<time_fromdt_tot and time1>time_todt_tot):
#     print("In between intervals")
#     print(time0 , time1)
#     print("    ")
#   elif time0>time_fromdt_tot and time1<time_todt_tot:
#     print("exeeding")
#     print(time0 , time1)
#     print("    ")
#   elif (time0<time_fromdt_tot or time0<time_todt_tot) and (time1>time_fromdt_tot or time1>time_todt_tot):
#     print("exceeding from left")
#     print(time0 , time1)
#     print("    ")
#   else:
#     print("not in between")  
#     print(time0 , time1)
#     print("    ")
















  # if not  time0 > time_fromdt_tot and time_todt_tot<time1:
  #   print("In between")
  #   print(time0 , time1)
  #   print("\n")
  # elif not time0<time_fromdt_tot or time1>time_todt_tot:
  #   print("exceeding")
  #   print(time0 , time1)
    
  # else:
  #   if not  time0 > time_fromdt_tot:
  #     print("not in between + exceeding")
  #     print(time0 , time1)
  #     print("\n")
  #   elif not time_todt_tot<time1:
  #     print("not in between + exceeding")
  #     print(time0 , time1)
  #     print("\n")
  #   else:
  #     print("not in between")
  #     print(time0 , time1)
  #     print("\n")