from prac import *





def load_image(image_File):
    img=Image.open(image_File)
    return img



# clean_db=pd.DataFrame(rows,columns=["Roll no","Name","Prac"])


with st.form(key="StudentData",clear_on_submit=True):
    input_rno=st.number_input("Enter Roll No",step=1)
    input_sname=st.text_input("Enter Student Name")
    input_standard=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
    image_File = st.file_uploader(label = "Upload file", type=["jpg","png"])
    submit_code=st.form_submit_button("Execute")


try:
    if submit_code:
        get_image_name=run_query(f"select * from student_data where photoURL like \"D:/3rd Year Project/3rd-year-project/Connecting SQL/ALL_IMAGES/{image_File.name}\"")
        get_sname=run_query(f"select * from student_data where StudentName like \"{input_sname}\" and studentstandard=\"{input_standard}\"")
        get_roll_no=run_query(f"select * from student_data where studentRollNo like {input_rno} and studentstandard=\"{input_standard}\"")
        if get_roll_no:
            st.error(f"Roll no {input_rno} already exists In standard {input_standard}")
        elif get_sname:
            st.error(f"Student name {input_sname} already exists In standard {input_standard}")
        elif get_image_name:
            st.error(f"Image {image_File.name} already exist.Use a different Image name")
        else:
            imageface=face_recognition.load_image_file(image_File)
            faceloc=face_recognition.face_locations(imageface)
            if faceloc:
                with open(os.path.join("D:\\3rd Year Project\\3rd-year-project\\Connecting SQL\\ALL_IMAGES",image_File.name),"wb") as f:
                    f.write(image_File.getbuffer())
                run_query(f"INSERT into student_data(studentrollno,StudentName,Studentstandard,photoURL) VALUES({input_rno},\"{input_sname}\",\"{input_standard}\",\"D:/3rd Year Project/3rd-year-project/Connecting SQL/ALL_IMAGES/{image_File.name}\")")
                st.success("Submitted")
            else:
                st.error("Face is required in image")
except:
    st.error("Fill all the Columns")