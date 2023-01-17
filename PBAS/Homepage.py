
from ast import Return
from cgi import test
from copy import deepcopy
import datetime
import imp
import importlib
import time
from re import I
from runpy import run_module
from tkinter import Frame
import cv2
import glob
import io
import pyodbc
import re
import hydralit_components as hc
from deepface import DeepFace
from turtle import clear
from matplotlib import image
from mysqlx import Column
import numpy as np
import streamlit as st
import mysql.connector
import dlib
import pandas as pd
import pickle as pkle
from PIL import Image,ImageEnhance
import os
from PIL import Image , ImageOps , ImageDraw , ImageFont
from typer import Exit
import face_recognition
import sys
from streamlit_option_menu import option_menu
import webbrowser
import yaml
import streamlit_authenticator as stauth
import pickle
from pathlib import Path

#viewing other pages in homepage:
      # sys.path.append("D:\\3rd Year Project\\3rd-year-project\\Connecting SQL\\pages")
      # func=__import__("01_Student")
      # selected_menu =option_menu(
      #   menu_title="Main Menu",
      #   options=["Home","Students","Teacher","Attendence"],
      #   orientation="horizontal"
      # )
      # if selected_menu=="Students":
      #   webbrowser.open("Student")
      #   #  st.markdown('<a href="Student" target="_self">Students</a>', unsafe_allow_html=True)
      #   # pkle.load(open('D:\\3rd Year Project\\3rd-year-project\\Connecting SQL\\pages\\01_Student.py', 'rb'))
      #   # url ="http://localhost:8501/Student"
      #   # webbrowser.open(url)

      # if selected_menu=="Home":
      #   st.write("Welcome to homepage")

# name_of_peeps=["jasraj"]
# usernames=["123"]

# file_path=Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("rb") as file:
#   hashed_passwords=pickle.load(file)

# authenticator = stauth.Authenticate(name_of_peeps,usernames,hashed_passwords,"adminlogin","abcdef")

# name , authentication_status , username = authenticator.login("Login","main")

# if authentication_status == False:
#   st.error("password incorrect")

# if authentication_status:


hashed_passwords = stauth.Hasher(['123', '456']).generate()
print(hashed_passwords)

with open('D:\\3rd Year Project\\3rd-year-project\\PBAS\\secrets.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if st.session_state["authentication_status"]:
    print("logged in successfully")
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
    
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')


weeklist=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# st.sidebar.markdown("Main page")

# st.title("hello")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jasrajsql",
  database="testdb"
)

myc=mydb.cursor()



def run_query(query):
    with mydb.cursor() as cur:
        cur.execute(query)
        data= cur.fetchall()
        mydb.commit()
        return data


def UserMessage(messagetype:str,UserMessage : str,timeForMessage:int):
    if messagetype == "error" or messagetype =="Error":
      message=st.error(UserMessage)
    elif messagetype == "success" or messagetype=="SUCCESS":
      message=st.success(UserMessage)
    elif messagetype == "warning" or messagetype=="Warning":
      message=st.warning(UserMessage)
    time.sleep(timeForMessage)
    message.empty()


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 












# query=run_query("select studentid from student_data where photourl =  \"D:/3rd Year Project/3rd-year-project/Connecting SQL/ALL_IMAGES/tf_1_2.jpg\" ")


# print(query[0][0])


# for queries in query:
#   print(queries[0])















    

    
            







