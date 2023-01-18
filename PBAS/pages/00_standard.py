import shutil
from Homepage import *






def add_standard():
    with st.form(key="Standard_Data",clear_on_submit=True):
            input_stdname=st.text_input("Enter Standard Name")
            submit_std=st.form_submit_button("Add Standard")

            

    if submit_std:
        if input_stdname is "":
            UserMessage("error",f"Enter A Valid Name",3)
            st.stop()
        input_stdname=input_stdname.upper()
        check_if_standard_exists=run_query(f"select * from standard_data where standard_name like \"{input_stdname}\"")
        if check_if_standard_exists:
            UserMessage("error","Standard already exists",3)
            st.stop()
        run_query(f"insert into standard_data(standard_name,is_enabled) Values(\"{input_stdname}\",1)")
        os.mkdir(f"D:\\3rd Year Project\\3rd-year-project\\PBAS\\Student_Images\\{str(input_stdname)}")
        UserMessage("success",f"{input_stdname} Added",3)
        
        

def view_standard():
    rows=run_query(f'''
    select standardid , standard_name from standard_data where is_enabled = 1
      ''')
    clean_db=pd.DataFrame(rows,columns=["ID","Standard"])
    st.dataframe(clean_db)

def delete_standard():
    rows = run_query(f'''
    select * from standard_data where is_enabled = 1
    ''')
    std_list_to_delete=[]
    for std in rows:
        std_list_to_delete.append(std[1])
    with st.form(key="delete_standard",clear_on_submit=True):
        input_standard=st.selectbox("Enter Standard To delete",std_list_to_delete)
        submit_code_for_standard_delete=st.form_submit_button("Submit")


    if submit_code_for_standard_delete:
        shutil.rmtree(f"D:\\3rd Year Project\\3rd-year-project\\PBAS\\Student_Images\\{str(input_standard)}") 
        run_query(f"Delete from standard_data where standard_name like \"{input_standard}\" ") 
        st.success(f"Standard {input_standard} deleted succesfully")




SelectedStudentMenu =option_menu(
  menu_title="Standard",
  menu_icon="list-task",
  options=["Add","View","Delete"],
  icons=["book","book","book"],
  orientation="horizontal"
)

if SelectedStudentMenu=="Add":
    add_standard()
elif SelectedStudentMenu=="View":
    view_standard()
elif SelectedStudentMenu=="Delete":
    delete_standard()