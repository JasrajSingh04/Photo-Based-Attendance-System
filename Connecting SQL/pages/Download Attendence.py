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


if set_date_button:
    if not stdlist:
        st.error("No lectures were there on the day")



with st.form(key="set_lecture"):
    lecturequery=run_query(f'''
    select distinct teacherlecture from attendence_Data
    inner join teacher_Data on teacher_data.teacherid=attendence_Data.att_teacherid
    where dateoflecture =\"{set_date}\" and teacherstandard=\"{std_of_student}\"
    ''')
    leclist=[]
    for datastd in lecturequery:
        lec=datastd[0]
        leclist.append(lec)
    lec_of_student=st.selectbox("Select Lecture",leclist)
    set_lecture_button=st.form_submit_button("Enter Lecture")


with st.form(key="get_Data"):
    submit_get_Data=st.form_submit_button("Get Data")


if submit_get_Data:
    df = run_query(f'''
        select studentname,teachername,teacherlecture, tt_fromtime,tt_totime , tt_standard,ispresent,dateoflecture
        from attendence_Data
        inner join student_data on student_data.studentid=attendence_Data.att_studentid
        inner join teacher_Data on teacher_data.teacherid=attendence_Data.att_teacherid
        inner join timetable_data on timetable_data.tt_id=attendence_Data.att_timetableid
        where dateoflecture =\"{set_date}\" and teacherstandard=\"{std_of_student}\" and teacherlecture=\"{lec_of_student}\"

            ''')

    query_result=pd.DataFrame(df)
    st.dataframe(query_result)
















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