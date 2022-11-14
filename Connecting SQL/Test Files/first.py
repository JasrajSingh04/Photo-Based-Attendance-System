
from glob import glob
from tkinter.tix import Tree
from turtle import heading
import mysql.connector
from dis import Instruction
from re import MULTILINE
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter
from xml.etree.ElementTree import Comment
import cv2
import os
import dlib
from tkinter.filedialog import askdirectory
from pip import main

from pyparsing import col


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jasrajsql",
  database="testdb"
)


mycursor = mydb.cursor()


win=tkinter.Tk()
win.title("Prac")
main_canvas=tkinter.Canvas(win,highlightthickness=1)
main_canvas.grid(columnspan=100,rowspan=100)
win.geometry("800x800")



def open_dt():
    global tree
    ca_popup=Toplevel(win)
    ca_popup.geometry("1000x300")
    ca_popup.title("Students of class A")
    main_canvas_top=tkinter.Canvas(ca_popup,width=300,height=300)
    main_canvas_top.grid(columnspan=2,rowspan=10)
    tree=ttk.Treeview(main_canvas_top,columns=("c1","c2","c3"),show="headings")
    tree.grid(row=1,column=1,padx=2)
    mycursor.execute("select * from student_ca")
    rows=mycursor.fetchall()
    for row in rows:
        tree.insert("",tkinter.END,values=row)
        tree.column("#1",anchor=tkinter.CENTER)
        tree.heading("#1",text="rollno")
        tree.column("#2",anchor=tkinter.CENTER)
        tree.heading("#2",text="studentname")
        tree.column("#3",anchor=tkinter.CENTER)
        tree.heading("#3",text="studentname")
        
        

button=tkinter.Button(main_canvas,text="show class A",command=open_dt)
button.grid(column=0,row=0,ipadx=10,columnspan=5)

tkinter.Label(main_canvas,text="   Enter New Student    ",font=('Arial', 13)).grid(row=1,column=0,columnspan=2,pady=10,)

input_rno=tkinter.Label(main_canvas,text="Roll No",font=('Arial', 13)).grid(row=2,column=0)
input_sname=tkinter.Label(main_canvas,text="Student Name",font=('Arial', 13)).grid(row=3,column=0)

e1=tkinter.Entry(main_canvas,width=20,font=('Arial', 15))
e2=tkinter.Entry(main_canvas,width=20,font=('Arial', 15))

e1.grid(row=2,column=2,ipadx=10,ipady=10)
e2.grid(row=3,column=2,pady=10,ipadx=10,ipady=10)




button=tkinter.Button(main_canvas,text="Add student to Class")
button.grid(column=1,row=5,ipadx=10)



win.mainloop()