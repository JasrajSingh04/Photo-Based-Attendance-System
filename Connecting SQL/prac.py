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





















    

    
            







