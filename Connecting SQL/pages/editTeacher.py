from prac import *


with st.form(key="TeacherData",clear_on_submit=True):
    input_teachername=st.text_input("Enter Teacher Name")
    input_teacherclass=st.text_input("Enter Lecture Name")
    teacherstandard=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
    submit_teacher=st.form_submit_button("Add")

if submit_teacher:
    run_query(f"Insert Into teacher_data(TeacherName,TeacherLecture,teacherstandard) VALUES (\"{input_teachername}\" , \"{input_teacherclass}\" , \"{teacherstandard}\")")
    st.success(f"Teacher name {input_teachername} added to teacher list ")
