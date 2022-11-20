from ast import Add
from logging import PlaceHolder
from queue import Full
from tkinter.messagebox import NO
from  Homepage import *





def AddTeacher():
    # st.title("Add Teacher Data")
    with st.form(key="TeacherData",clear_on_submit=True):
        input_teachername=st.text_input("Enter First Name")
        input_teachername_2=st.text_input("Enter Last Name")
        input_teacherclass=st.text_input("Enter Lecture Name")
        teacherstandard=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
        submit_teacher=st.form_submit_button("Add")

    if submit_teacher:
        if not input_teachername == "" and not input_teachername_2 == "" and not input_teacherclass =="":
            FullTeacherName=input_teachername.capitalize() +" "+ input_teachername_2.capitalize()
            FullTeacherName=re.sub(' +', ' ',FullTeacherName)
            input_teacherclass=re.sub(' +', ' ',input_teacherclass)
            input_teacherclass = input_teacherclass.rstrip()
            
            check_if_teacher_exists=run_query(f"select *  from  teacher_data where teachername like \"{FullTeacherName}\" and Teacherlecture like \"{input_teacherclass.upper()}\" and Teacherstandard like \"{teacherstandard}\"")
            
            if check_if_teacher_exists:
                UserMessage(messagetype="error",UserMessage=f"There is already a teacher named {FullTeacherName} of class {teacherstandard} with lecture {input_teacherclass.upper()}",timeForMessage=3) 

            else:
                run_query(f"Insert Into teacher_data(TeacherName,TeacherLecture,teacherstandard) VALUES (\"{FullTeacherName}\" , \"{input_teacherclass.upper()}\" , \"{teacherstandard}\")")
                UserMessage(messagetype="success",UserMessage=f"Teacher name {FullTeacherName} added to teacher list",timeForMessage=3) 
                st.experimental_rerun()
                
        else:
            UserMessage("error","Fill all the fields",3)




def ViewTeacher():
    # st.title("Show Teacher Data")
    with st.form(key="viewTeacherData",clear_on_submit=True):
        teacherstandard=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
        submit_viewteacherdata=st.form_submit_button("View")  

    if submit_viewteacherdata:
      rows=run_query(f"Select teachername,teacherlecture,teacherstandard from teacher_Data where teacherstandard=\"{teacherstandard}\"")
      clean_db=pd.DataFrame(rows,columns=["Teacher Name","Teacher Lecture","Teacher Standard"])
      st.write(f"Viewing Data For {teacherstandard}")
      st.dataframe(clean_db)



def DeleteTeacher():
    # st.markdown("# Delete Teacher")
    with st.form(key="GettingTeacherStandard"):
        input_standard=st.selectbox("Enter Standard",["Select a Standard","FYIT","SYIT","TYIT"])
        SubmitViewTeacherData=st.form_submit_button("Submit")
    
    with st.form(key="GettingTeacherName"):
        st.write("Note: Deleting A teacher from data will also Delete all the lectures from timetable of that teacher")
        TeacherName=run_query(f"select distinct teachername from teacher_data where teacherstandard like \"{input_standard}\"")
        ListOfNames=[]
        for names in TeacherName:
            TeacherNameFor=names[0]
            ListOfNames.append(TeacherNameFor)
        TeacherNameSeLect=st.selectbox("Enter Name",ListOfNames)
        SubmitGettingTeacherName=st.form_submit_button("Submit")
    
  

    if SubmitGettingTeacherName:
        if input_standard  and TeacherNameSeLect :
            run_query("SET FOREIGN_KEY_CHECKS=0")
            run_query(f'''delete t from timetable_data t
            inner join teacher_data e on t.tt_lecturename = e.teacherid 
            where e.TeacherName = \"{TeacherNameSeLect}\"''')
            run_query(f"delete from teacher_data where teachername=\"{TeacherNameSeLect}\" and teacherstandard=\"{input_standard}\"")
            run_query("SET FOREIGN_KEY_CHECKS=1")
            
            UserMessage(messagetype="success",UserMessage=f"Deleted {TeacherNameSeLect} from {input_standard}",timeForMessage=3)
            st.experimental_rerun()
        else:
            UserMessage(messagetype="error",UserMessage="Select a Teacher that needs to be deleted",timeForMessage=3)
            
            




# page_names_to_funcs = {
#     "Add Teacher Data": AddTeacher,
#     "View Teacher Data": ViewTeacher,
#     "Delete Teacher Data": DeleteTeacher,
# }



# selected_page = st.sidebar.radio("Select a page", page_names_to_funcs.keys(),index=0)
# page_names_to_funcs[selected_page]()


SelectedMenuTeacher =option_menu(
  menu_title="Teacher",
  menu_icon="list-task",
  options=["Add","View","Delete"],
  icons=["book","book","book"],
  orientation="horizontal"
)


if SelectedMenuTeacher=="Add":
    AddTeacher()
elif SelectedMenuTeacher=="View":
    ViewTeacher()
elif SelectedMenuTeacher=="Delete":
    DeleteTeacher()