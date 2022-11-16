from aiohttp import DataQueue
from  Homepage import *

clean_db = pd.DataFrame

with st.form(key="set_date"):
    set_date=st.date_input("Select Attendence Date",datetime.date.today())
    set_date_button=st.form_submit_button("Enter Date")




with st.form(key="set_standard",clear_on_submit=False):
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
    set_standard_button=st.form_submit_button("Submit Standard")

if set_standard_button:
    if not stdlist:
        st.error("No lectures were there on the day")
    rows=run_query(f'''
    select StudentRollNo,studentname,teachername,teacherlecture,tt_fromtime,tt_totime,ispresent 
    from attendence_data
    inner join student_data on student_data.Studentid=attendence_data.att_studentid
    inner join teacher_data on teacher_data.teacherid=attendence_data.att_teacherID
    inner join timetable_data on timetable_data.tt_id=attendence_data.att_timetableid
    where teacherstandard=\"{std_of_student}\" and dateoflecture=\"{set_date}\" ;
    ''')
    clean_db=pd.DataFrame(rows,columns=["Roll No","Student Name","Teacher Name","Lecture","From","To","Present"])
    clean_db.sort_values(by=["Roll No"],ascending=True)
    df=st.dataframe(clean_db)
                                                                                                                                                                                                                                                                                           
    #csv file df
    with st.spinner("Wait for the file to be downloaded"):
        sql_query=pd.read_sql_query(f''' 
        select StudentRollNo,studentname,teachername,teacherlecture,tt_fromtime,tt_totime,ispresent 
        from attendence_data
        inner join student_data on student_data.Studentid=attendence_data.att_studentid
        inner join teacher_data on teacher_data.teacherid=attendence_data.att_teacherID
        inner join timetable_data on timetable_data.tt_id=attendence_data.att_timetableid
        where teacherstandard=\"{std_of_student}\" and dateoflecture=\"{set_date}\" ;
        ''',mydb)
        TimeInDataName=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        DataToCSV=pd.DataFrame(sql_query)
        Dataname=str(set_date)+" "+str(std_of_student)+" "+str(TimeInDataName)
        CSVpath=fr"D:\3rd Year Project\3rd-year-project\Connecting SQL\Attendance Data Downloaded\{Dataname}.csv"
        DataToCSV.to_csv(CSVpath,index=False, header=True)
        time.sleep(3)
    UserMessage("success","File Saved",3)
    with open(CSVpath) as f:
        st.download_button("Download CSV",f,f"{Dataname}.csv")


# with st.form(key="Set Standard",clear_on_submit=False):
#     if clean_db.empty:
#         verifyDf=False
#         st.write("...Waiting For Data")
#     else:
#         verifyDf=True
#         st.write("Click on button download")
#     submit_download_request=st.form_submit_button("Download")


# if submit_download_request and verifyDf is False:
#     UserMessage("error","First Select The Data First",3)
#     st.stop()

    