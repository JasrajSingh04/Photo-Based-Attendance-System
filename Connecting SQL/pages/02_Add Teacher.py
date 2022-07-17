from prac import *





def main_page():
    st.title("Add Teacher Data")
    with st.form(key="TeacherData",clear_on_submit=True):
        input_teachername=st.text_input("Enter Teacher Name")
        input_teacherclass=st.text_input("Enter Lecture Name")
        teacherstandard=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
        submit_teacher=st.form_submit_button("Add")

    if submit_teacher:
        check_if_teacher_exists=run_query(f"select *  from  teacher_data where teachername like \"{input_teachername}\" and Teacherlecture like \"{input_teacherclass}\" and Teacherstandard like \"{teacherstandard}\"")
        print(check_if_teacher_exists)
        if check_if_teacher_exists:
            st.error(f"There is already a teacher named {input_teachername} of class {teacherstandard} with lecture {input_teacherclass}")
        else:
            run_query(f"Insert Into teacher_data(TeacherName,TeacherLecture,teacherstandard) VALUES (\"{input_teachername}\" , \"{input_teacherclass}\" , \"{teacherstandard}\")")
        st.success(f"Teacher name {input_teachername} added to teacher list ")




def page2():
    st.title("Show Teacher Data")
    with st.form(key="viewTeacherData",clear_on_submit=True):
        teacherstandard=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
        submit_viewteacherdata=st.form_submit_button("Add")  

    if submit_viewteacherdata:
      rows=run_query(f"Select teachername,teacherlecture,teacherstandard from teacher_Data where teacherstandard=\"{teacherstandard}\"")
      clean_db=pd.DataFrame(rows,columns=["Teacher Name","Teacher Lecture","Teacher Standard"])
      st.dataframe(clean_db)



def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Add Data": main_page,
    "View Data": page2,
    "Delete Data": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()