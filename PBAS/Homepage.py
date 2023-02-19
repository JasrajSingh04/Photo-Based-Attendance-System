
from ast import Return
from cgi import test
import collections
from copy import deepcopy
import datetime
import imp
import importlib
from streamlit.web.server import Server
import json
import time
from re import I
from runpy import run_module
from tkinter import Frame
import cv2
import glob
import io
import pyodbc
import re
import handout
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
import requests
from pathlib import Path
import extra_streamlit_components as stx
from streamlit.source_util import _on_pages_changed, get_pages
import extra_streamlit_components as stx
from collections import defaultdict
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


DEFAULT_PAGE ="Homepage.py"

def get_all_pages():
    default_pages = get_pages(DEFAULT_PAGE)

    pages_path = Path("pages.json")

    if pages_path.exists():
        saved_default_pages = json.loads(pages_path.read_text())
    else:
        saved_default_pages = default_pages.copy()
        pages_path.write_text(json.dumps(default_pages, indent=4))

    return saved_default_pages


def clear_all_but_first_page():
    current_pages = get_pages(DEFAULT_PAGE)

    if len(current_pages.keys()) == 1:
        return

    get_all_pages()

    # Remove all but the first page
    key, val = list(current_pages.items())[0]
    current_pages.clear()
    current_pages[key] = val

    _on_pages_changed.send()


def show_all_pages():
    current_pages = get_pages(DEFAULT_PAGE)

    saved_pages = get_all_pages()

    # Replace all the missing pages
    for key in saved_pages:
        if key not in current_pages:
            current_pages[key] = saved_pages[key]

    _on_pages_changed.send()


def hide_page(name: str):
    current_pages = get_pages(DEFAULT_PAGE)

    for key, val in current_pages.items():
        if val["page_name"] == name:
            del current_pages[key]
            _on_pages_changed.send()
            break


clear_all_but_first_page()

































def get_cookie_manager_homepage():
    return stx.CookieManager(key="homepage_")

cookie_manager_stx = get_cookie_manager_homepage()
cookie_value = cookie_manager_stx.get(cookie="some_cookie_name")


def login():
#   username="yes_1"
#   name_="yes"
#   password_="$2b$12$jXLLLINDm2safqPdfy3Oc..HCum6rSC6Dbrxsw1q7GDC46BTbrdkG"
#   usernames=[username]
#   names=[name_]
#   passwords=[password_]
#   hashed=stauth.Hasher(passwords=passwords).generate()
#   credentials = {
#             "usernames":{
#                 []:{
#                     "name":[],
#                     "password":[]
#                     },      
#                 }
#             }
#   nesteddict=lambda:defaultdict(nesteddict)
#   credentials=nesteddict()
#   test_button=st.button("submit")
#   if test_button:
#      for nums in range(5,10000):
#         hashed_num = stauth.Hasher([f"rows{nums}"]).generate()
#         run_query(f'''INSERT into users(name,username,password) Values("rows{nums}","rows{nums}","{hashed_num[0]}")''')
  credentials_dict=dict()
  userQuery=run_query("Select username,name,password from users")
  for rows in userQuery:
    credentials_dict[rows[0]]={"name":rows[1],"password":rows[2]}
  

    #  credentials["credentials"]["usernames"][f"{rows[0]}"]["name"]=rows[1]
    #  credentials["credentials"]["usernames"][f"{rows[0]}"]["password"]=rows[2]
    #  credentials.update({
    #         "usernames":{
    #             rows[0]:{
    #                 "name":rows[1],
    #                 "password":rows[2]
    #                 },      
    #             }
    #         })
  credentials=dict({"usernames":credentials_dict})
#   print(credentials)  
  

 
  authenticator = stauth.Authenticate(
      credentials,"some_cookie_name","somesignaturekey",cookie_expiry_days=30
  )
  name, authentication_status, username = authenticator.login('Login', 'main')
    

  if st.session_state["authentication_status"] and cookie_value is not None: 
      authenticator.logout('Logout', 'main')
      st.write(f'Welcome *{st.session_state["name"]}*')
      st.title('Some content')
    
  elif st.session_state["authentication_status"] == False:
      st.error('Username/password is incorrect')
  elif st.session_state["authentication_status"] == None:
      st.warning('Please enter your username and password')

# st.sidebar.write("hello")

def signup():
  # def get_cookie_manager():
  #     return stx.CookieManager()

  # cookie_manager_stx = get_cookie_manager()
  # cookie_value = cookie_manager_stx.get(cookie="some_cookie_name")
  
  # if cookie_value is not None:
  #    st.write("Already Signed In")
  #    st.stop()
  with st.form(key="Signup",clear_on_submit=True):
    input_name=st.text_input("Enter Name")
    input_username=st.text_input("Enter Username")
    input_password=st.text_input("Enter Password",type="password")
    submit_sign=st.form_submit_button("Submit")

    hashed_passwords = stauth.Hasher([input_password]).generate()
  
    if submit_sign:
      try:
        run_query(f'''INSERT into users(name,username,password) Values("{input_name}","{input_username}","{hashed_passwords[0]}")''')
        UserMessage("success",f"Succesfully registered {input_username}",3) 
      except mysql.connector.IntegrityError as err:
         UserMessage("error","Username Already Exists",3)
      


weeklist=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# st.sidebar.markdown("Main page")

# st.title("hello")



def UserMessage(messagetype:str,UserMessage : str,timeForMessage:int):
    if messagetype == "error" or messagetype =="Error":
      message=st.error(UserMessage)
    elif messagetype == "success" or messagetype=="SUCCESS":
      message=st.success(UserMessage)
    elif messagetype == "warning" or messagetype=="Warning":
      message=st.warning(UserMessage)
    time.sleep(timeForMessage)
    message.empty()

# signin_btn=st.button("Login")
# signup_btn=st.button("new? signup")


if cookie_value is None:
  clear_all_but_first_page()
  SelectedPageMenu =option_menu(
  menu_title="Account",
  menu_icon="list-task",
  options=["Login","Sign In"],
  icons=["book","book"],
  orientation="horizontal"
  )

  if SelectedPageMenu=="Login":
      login()
  elif SelectedPageMenu=="Sign In":
      signup()
else:
   show_all_pages()
   hide_page(DEFAULT_PAGE.replace(".py", ""))
   login()

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















    

    
            







