import functools
from queue import Full
from tkinter import Button
from fastapi import Query

from numpy import full
from  Homepage import *
import re




def load_image(image_File):
    img=Image.open(image_File)
    return img



# clean_db=pd.DataFrame(rows,columns=["Roll no","Name","Prac"])

def AddStudent():
   st.title("Add Data")
   with st.form(key="StudentData",clear_on_submit=True):
    input_rno=st.number_input("Enter Roll No",step=1,min_value=1)
    input_sname=st.text_input("Enter First Name")
    input_sname_2=st.text_input("Enter Last Name")
    input_standard=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
    image_File = st.file_uploader(label = "Upload file", type=["jpg","png"])
    submit_code=st.form_submit_button("Execute")


    if submit_code:
        FullNameOfStudent=input_sname.capitalize()+" "+ input_sname_2.capitalize()
        FullNameOfStudent=re.sub(' +', ' ',FullNameOfStudent)
        get_image_name=run_query(f"select * from student_data where photoURL like \"D:/3rd Year Project/3rd-year-project/Connecting SQL/ALL_IMAGES/{image_File.name}\"")
        get_sname=run_query(f"select * from student_data where StudentName like \"{FullNameOfStudent}\" and studentstandard=\"{input_standard}\"")
        get_roll_no=run_query(f"select * from student_data where studentRollNo like {input_rno} and studentstandard=\"{input_standard}\"")
        if get_roll_no:
            st.error(f"Roll no {input_rno} already exists In standard {input_standard}")
        elif get_sname:
            st.error(f"Student name {FullNameOfStudent} already exists In standard {input_standard}")
        elif get_image_name:
            st.error(f"Image {image_File.name} already exist.Use a different Image name")
        else:
            imageface=face_recognition.load_image_file(image_File)
            faceloc=face_recognition.face_locations(imageface)
            if faceloc:
                with open(os.path.join("D:\\3rd Year Project\\3rd-year-project\\Connecting SQL\\ALL_IMAGES",image_File.name),"wb") as f:
                    f.write(image_File.getbuffer())
                run_query(f"INSERT into student_data(studentrollno,StudentName,Studentstandard,photoURL) VALUES({input_rno},\"{FullNameOfStudent}\",\"{input_standard}\",\"D:/3rd Year Project/3rd-year-project/Connecting SQL/ALL_IMAGES/{image_File.name}\")")
                st.success("Submitted")
            else:
                st.error("Face is required in image")
                
    


def ViewStudent():
    st.title("View Data")
    with st.form(key="viewStudentData"):
        input_standard=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
        SubmitViewStudentData=st.form_submit_button("View")
    
    if SubmitViewStudentData:
      rows=run_query(f"Select studentrollno , studentname, studentstandard from student_data where studentstandard=\"{input_standard}\"")
      clean_db=pd.DataFrame(rows,columns=["Roll No","Student Name","Standard"])
      st.write(f"Viewing Data For {input_standard}")
      st.dataframe(clean_db)

def DeleteStudent():
    st.markdown("# Delete Student")
    with st.form(key="GettingStudentStandard"):
        input_standard=st.selectbox("Enter Standard",["Select a Name","FYIT","SYIT","TYIT"])
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
        try:
            photoURL=run_query(f"select photourl from student_data where studentname like \"{StudentNameSeLect}\" and studentstandard like \"{input_standard}\" ")
            for url in photoURL:
                os.remove(url[0])
        except:
            pass
        run_query("SET FOREIGN_KEY_CHECKS=0")
        run_query(f"delete from student_data where studentname=\"{StudentNameSeLect}\" and studentstandard=\"{input_standard}\"")
        run_query("SET FOREIGN_KEY_CHECKS=1")
        st.success(f"{StudentNameSeLect} was removed")
        
        



page_names_to_funcs = {
    "Add Student Data": AddStudent,
    "View Student Data": ViewStudent,
    "Delete Student Data": DeleteStudent,
}

selected_page = st.sidebar.radio("Select a page", page_names_to_funcs.keys(),index=0)
page_names_to_funcs[selected_page]()
