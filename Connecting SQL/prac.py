from ast import Return
import imp
import io
from mysqlx import Column
import streamlit as st
import mysql.connector
import pandas as pd
from PIL import Image,ImageEnhance
import os
from PIL import Image , ImageOps , ImageDraw , ImageFont
from typer import Exit
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

with st.form(key="query_form"):
    input_rno=st.number_input("Enter Roll No",min_value=1, max_value=50, step=1)
    input_sname=st.text_input("Enter Student Name")
    image_File = st.file_uploader(label = "Upload file", type=["jpg"])
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
        img = load_image(image_File)
        with open(os.path.join("D:\\3rd Year Project\\3rd-year-project\\Connecting SQL\\SQL FILES IMAGES",image_File.name),"wb") as f:
            f.write(image_File.getbuffer())
        run_query(f"INSERT into student_CA(rollno,StudentName,photo_link) VALUES({input_rno},\"{input_sname}\",\"D:/3rd Year Project/3rd-year-project/Connecting SQL/SQL FILES IMAGES/{image_File.name}\")")
        st.success("Submitted")




