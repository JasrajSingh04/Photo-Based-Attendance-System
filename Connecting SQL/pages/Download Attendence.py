from aiohttp import DataQueue
from prac import *



with st.form(key="set_date"):
    set_date=st.date_input("Select Attendence Date",datetime.date.today())
    set_date_button=st.form_submit_button("Enter Date")


with st.form(key="set_standard"):
    datequery=run_query(f'''
    select distinct tt_standard from attendence_Data
    inner join timetable_data on timetable_data.tt_id=attendence_Data.att_timetableid
    where dateoflecture = \"{set_date}\"
    ''')
    stdlist=[]
    for data in datequery:
        std=data[0]
        stdlist.append(std)
    std_of_student=st.selectbox("Select Standard",stdlist)
    set_standard_button=st.form_submit_button("Enter Standard")


    





















# with st.form(key="lec_form",clear_on_submit=True):
#     input_lecname=st.text_input("Enter Student Name")
#     submit_lec=st.form_submit_button("Add lecture")



# try:
#     if submit_lec:
#         if input_lecname=="":
#             st.error("Enter Lecture Name")
#         else:
#             run_query(f"insert into lnames(lecture_name) VALUES(\"{input_lecname}\")")
#             st.success(f"{input_lecname} Added to Lecture list")
# except:
#     st.error("Enter Lecture Name")
 

# rows=run_query("Select * from lnames")
# clean_db=pd.DataFrame(rows,columns=["Lecture Names"])
# st.dataframe(clean_db)