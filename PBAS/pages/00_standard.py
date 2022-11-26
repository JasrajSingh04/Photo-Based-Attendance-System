from Homepage import *




def add_standard():
    with st.form(key="Standard_Data",clear_on_submit=True):
            input_stdname=st.text_input("Enter Standard Name")
            submit_std=st.form_submit_button("Add Standard")
            

    if submit_std:
        input_stdname=input_stdname.upper()
        run_query(f"insert into standard_data(standard_name) Values(\"{input_stdname}\")")
        UserMessage("success",f"{input_stdname} Added",3)
        

def view_standard():
    rows=run_query(f'''
    select * from standard_data
      ''')
    clean_db=pd.DataFrame(rows,columns=["ID","Standard"])
    st.dataframe(clean_db)

def delete_standard():
    print("")


SelectedStudentMenu =option_menu(
  menu_title="Teacher",
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