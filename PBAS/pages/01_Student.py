from email import message
import functools
from queue import Full
from tkinter import Button, Menu
from fastapi import Query

from numpy import full
from pydantic import DurationError
from  Homepage import *
import re






def load_image(image_File):
    img=Image.open(image_File)
    return img



# clean_db=pd.DataFrame(rows,columns=["Roll no","Name","Prac"])

def AddStudent():
    # st.title("Add Data")

    with st.form(key="StudentData",clear_on_submit=True):
        std=run_query("select standard_name from standard_data")
        stdlist=[]
        for std_name in std:
            stdlist.append(std_name[0])
        input_rno=st.number_input("Enter Roll No",step=1,min_value=1)
        input_sname=st.text_input("Enter First Name")
        input_sname_2=st.text_input("Enter Last Name")
        input_standard=st.selectbox("Enter Standard",stdlist)
        image_File = st.file_uploader(label = "Upload file", type=["jpg","png"])
        submit_code=st.form_submit_button("Execute")


    if submit_code:
        if not input_rno=="" and not input_sname =="" and not input_sname_2 =="" and not input_standard =="" and image_File is not None:

            FullNameOfStudent=input_sname.capitalize()+" "+ input_sname_2.capitalize()
            FullNameOfStudent=re.sub(' +', ' ',FullNameOfStudent)
            FullNameOfStudent=FullNameOfStudent.rstrip()
            
            
            get_image_name=run_query(f"select * from student_data where photoURL like \"D:/3rd Year Project/3rd-year-project/PBAS/Student_Images/{input_standard}/{image_File.name}\"")
            get_sname=run_query(f"select * from student_data where StudentName like \"{FullNameOfStudent}\" and studentstandard=\"{input_standard}\"")
            get_roll_no=run_query(f"select * from student_data where studentRollNo like {input_rno} and studentstandard=\"{input_standard}\"")
            
            
            if get_roll_no:
                UserMessage(messagetype="error",UserMessage=f"Roll no {input_rno} already exists In standard {input_standard}",timeForMessage=3)

            elif get_sname:
                UserMessage(messagetype="error",UserMessage=f"Student name {FullNameOfStudent} already exists In standard {input_standard}",timeForMessage=3)

            elif get_image_name:
                UserMessage(messagetype="error",UserMessage=f"Image {image_File.name} already exist.Use a different Image name",timeForMessage=3)

            else:
                imageface=face_recognition.load_image_file(image_File)
                faceloc=face_recognition.face_locations(imageface)
                if faceloc:
                    if len(faceloc) >1 :
                        UserMessage(messagetype="error",UserMessage="Multiple faces detected",timeForMessage=3)
                    else:

                        with open(os.path.join(f"D:\\3rd Year Project\\3rd-year-project\\PBAS\\Student_Images\\{input_standard}",image_File.name),"wb") as f:
                            f.write(image_File.getbuffer())
                        run_query(f"INSERT into student_data(studentrollno,StudentName,Studentstandard,photoURL) VALUES({input_rno},\"{FullNameOfStudent}\",\"{input_standard}\",\"D:/3rd Year Project/3rd-year-project/PBAS/Student_Images/{input_standard}/{image_File.name}\")")
                    
                        UserMessage(messagetype="success", UserMessage=f"Student {FullNameOfStudent} added to {input_standard}",timeForMessage=3)
                else:
                    UserMessage("error","Face is required in an image",3)
        else:
            UserMessage(messagetype="error",UserMessage="Fill all the fields",timeForMessage=3)        


def ViewStudent():
    # st.title("View Data")
    with st.form(key="viewStudentData"):
        std=run_query("select standard_name from standard_data")
        stdlist=[]
        for std_name in std:
            stdlist.append(std_name[0])
        input_standard=st.selectbox("Enter Standard",stdlist)
        SubmitViewStudentData=st.form_submit_button("View")
    
    if SubmitViewStudentData:
      rows=run_query(f"Select studentrollno , studentname, studentstandard from student_data where studentstandard=\"{input_standard}\"")
      clean_db=pd.DataFrame(rows,columns=["Roll No","Student Name","Standard"])
      st.write(f"Viewing Data For {input_standard}")
      st.dataframe(clean_db)



def DeleteStudent():
    # st.markdown("# Delete Student")
    with st.form(key="GettingStudentStandard"):
        std=run_query("select standard_name from standard_data")
        stdlist=[]
        for std_name in std:
            stdlist.append(std_name[0])
        input_standard=st.selectbox("Enter Standard",stdlist)
        SubmitViewStudentData=st.form_submit_button("Submit")
    
    with st.form(key="GettingStudentName"):
        StudentName=run_query(f"select studentname from student_data where studentstandard like \"{input_standard}\"")
        ListOfNames=[]
        for names in StudentName:
            StudentNameFor=names[0]
            ListOfNames.append(StudentNameFor)
        StudentNameSeLect=st.selectbox("Enter Name",ListOfNames)
        SubmitGettingStudentName=st.form_submit_button("Submit")
    
    if SubmitGettingStudentName:
        if StudentNameSeLect is None:
            UserMessage("error","Select the Student Name that needs to be deleted",3)
            st.stop()
        try:
            photoURL=run_query(f"select photourl from student_data where studentname like \"{StudentNameSeLect}\" and studentstandard like \"{input_standard}\" ")
            for url in photoURL:
                os.remove(url[0])
        except:
            pass
        run_query("SET FOREIGN_KEY_CHECKS=0")
        run_query(f"delete from student_data where studentname=\"{StudentNameSeLect}\" and studentstandard=\"{input_standard}\"")
        run_query("SET FOREIGN_KEY_CHECKS=1")
        UserMessage(messagetype="success",UserMessage=f"{StudentNameSeLect} was removed from {input_standard}",timeForMessage=3)    
       
        


SelectedMenuStudents =option_menu(
  menu_title="Student",
  menu_icon="list-task",
  options=["Add","View","Delete"],
  icons=["book","book","book"],
  orientation="horizontal"
)


if SelectedMenuStudents=="Add":
    AddStudent()
elif SelectedMenuStudents=="View":
    ViewStudent()
elif SelectedMenuStudents=="Delete":
    DeleteStudent()


