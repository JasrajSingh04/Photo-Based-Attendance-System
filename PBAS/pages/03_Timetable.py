from ast import Delete, With
from lib2to3.pytree import convert
from pickle import TRUE
from tkinter.tix import Select
from tracemalloc import start
from pandas import to_datetime

from regex import W
from requests import delete
from  Homepage import *





def AddTT():
    with st.form(key="standard_selection"):
        std=run_query("select standard_name from standard_data")
        stdlist=[]
        for std_name in std:
            stdlist.append(std_name[0])
        standard_sel=st.selectbox("Enter Standard",stdlist)
        submit_standard_selection=st.form_submit_button("Submit Standard")


    with st.form(key="Timetable",clear_on_submit=True):
        lect_data=run_query(f"select distinct Teacherlecture from teacher_data where teacherstandard=\"{standard_sel}\" ")
        lectureslist=[]
        for lect in lect_data:
            lnamefor=lect[0]
            lectureslist.append(lnamefor)
        input_ttname=st.selectbox("Enter Lecture Name",lectureslist)
        submit_teacher_name=st.form_submit_button("Select Lecture")
    
    

    with st.form(key="Teacher_name"):
        Teacher_name_data=run_query(f"select teachername from teacher_data where teacherstandard like \"{standard_sel}\" and teacherlecture like \"{input_ttname}\"")
        teachernamelist=[]
        for teachername in Teacher_name_data:
            teachernamefor=teachername[0]
            teachernamelist.append(teachernamefor)
        input_TeacherName=st.selectbox("Enter Teacher Name",teachernamelist)
        SelectWeekDay=st.selectbox("Enter Day of the week",weeklist)
        col1, col2 = st.columns([1,1])
        with col1:
            start_time=st.time_input("From",datetime.time(8, 45))
        with col2:
            end_time=st.time_input("To",datetime.time(8, 45))
        submit_timetable=st.form_submit_button("Add lecture Data")

    if submit_timetable:
        if standard_sel  and input_ttname and  input_TeacherName:
            time_fromdt_tot=start_time
            time_todt_tot=end_time
            timeistrue=False
            if not start_time<end_time:
                # st.error("time error")
                UserMessage(messagetype="error",UserMessage="The end time of lecture cannot be before the start time",timeForMessage=3)
            else:
                ttname_tokey=run_query(f"select teacherid from teacher_data where teacherlecture = \"{input_ttname}\" and teachername=\"{input_TeacherName}\"  ")
                for key in ttname_tokey:
                    mainkey=key[0]
                print(mainkey)
                time_query=run_query(f"select tt_fromtime , tt_totime from timetable_data where tt_standard=\"{standard_sel}\" and tt_dayofweek=\"{SelectWeekDay}\"")

                check_query=run_query(f"select * from timetable_data where tt_fromtime=\"{start_time}\" and tt_totime=\"{end_time}\" and tt_standard=\"{standard_sel}\" and tt_lecturename like {mainkey} and tt_dayofweek like \"{SelectWeekDay}\"")
                
                if check_query:
                    UserMessage("error",f"There is already a lecture named {input_ttname} with timings from {start_time} to {end_time} of standard {standard_sel} with teacher {input_TeacherName}",3)
                    st.stop()
                
                if time_query:
                    for time in time_query:
                        time0=datetime.datetime.strptime(time[0], '%H:%M:%S').time()
                        time1=datetime.datetime.strptime(time[1], '%H:%M:%S').time()
                        # if check_query:
                        #     st.error(f"There is Already a lecture from {time[0]} to {time[1]} of condition 1")
                        #     timeistrue=False
                        #     break
                        if (time0<time_fromdt_tot and time1>time_todt_tot):
                            # st.error(f"There is Already a lecture from {time[0]} to {time[1]} of condition 2")
                            UserMessage(messagetype="error",UserMessage=f"There is Already a lecture from {time[0]} to {time[1]}",timeForMessage=3)
                            timeistrue=False
                            break
                        elif time0>time_fromdt_tot and time1<time_todt_tot:
                            UserMessage(messagetype="error",UserMessage=f"There is Already a lecture from {time[0]} to {time[1]}",timeForMessage=3)
                            # st.error(f"There is Already a lecture from {time[0]} to {time[1]} of condition 3")
                            timeistrue=False
                            break
                        elif (time0<time_fromdt_tot or time0<time_todt_tot) and (time1>time_fromdt_tot or time1>time_todt_tot):
                            UserMessage(messagetype="error",UserMessage=f"There is Already a lecture from {time[0]} to {time[1]}",timeForMessage=3)
                            # st.error(f"There is Already a lecture from {time[0]} to {time[1]} of condition 4")
                            timeistrue=False
                            break
                        else:
                            timeistrue=True  
                            pass
                else:
                    run_query(f"Insert into timetable_data(tt_lecturename,tt_fromtime,tt_totime,tt_standard,tt_Dayofweek) VALUES ( {mainkey} , \"{start_time}\" , \"{end_time}\" , \"{standard_sel}\" , \"{SelectWeekDay}\")")
                    # st.success(f"{input_ttname} Added to time table")
                    UserMessage(messagetype="success",UserMessage=f"{input_ttname} Added to time table",timeForMessage=3)
                    # st.success("time query was not none")


                if timeistrue is True:

                    if(time0<time_todt_tot and time1<time_todt_tot):

                        run_query(f"Insert into timetable_data(tt_lecturename,tt_fromtime,tt_totime,tt_standard,tt_Dayofweek) VALUES ( {mainkey} , \"{start_time}\" , \"{end_time}\" , \"{standard_sel}\" , \"{SelectWeekDay}\")")
                        UserMessage(messagetype="success",UserMessage=f"{input_ttname} Added to time table",timeForMessage=3)

                    if  (time0>time_fromdt_tot and time1>time_fromdt_tot):

                        run_query(f"Insert into timetable_data(tt_lecturename,tt_fromtime,tt_totime,tt_standard,tt_Dayofweek) VALUES ( {mainkey} , \"{start_time}\" , \"{end_time}\" , \"{standard_sel}\" , \"{SelectWeekDay}\")")
                        UserMessage(messagetype="success",UserMessage=f"{input_ttname} Added to time table",timeForMessage=3)
    
        else:
             UserMessage("error","Fill all the fields",3)
     
def ViewTT():
    with st.form(key="viewTimetableData"):
        std=run_query("select standard_name from standard_data")
        stdlist=[]
        for std_name in std:
            stdlist.append(std_name[0])
        input_standard=st.selectbox("Enter Standard",stdlist)
        SelectWeekDay=st.selectbox("Enter Day of the week",weeklist)
        SubmitViewTimetableData=st.form_submit_button("View")
    
    if SubmitViewTimetableData:
      rows=run_query(f'''
    select teacher_data.teachername ,teacher_data.teacherLecture,timetable_Data.tt_fromtime, timetable_Data.tt_totime,timetable_Data.tt_standard ,timetable_data.tt_dayofweek
    from timetable_data 
    inner join teacher_data on timetable_data.tt_lecturename=teacher_data.teacherid where timetable_data.tt_standard=\"{input_standard}\" and timetable_data.tt_dayofweek=\"{SelectWeekDay}\";
      ''')
      clean_db=pd.DataFrame(rows,columns=["Teachername","Lecture Name","From","To","Standard","Day of Week"])
      st.dataframe(clean_db)






def DeleteTT():
    st.markdown("Delete Lectures")
    with st.form(key="StandardTimeTable"):
        std=run_query("select standard_name from standard_data")
        stdlist=[]
        for std_name in std:
            stdlist.append(std_name[0])
        TimeTableDeleteStandard=st.selectbox("Enter Standard",stdlist)
        TimeTableWeekDaySelect=st.selectbox("Enter day of the week",weeklist)
        SubmitTimeTableStandard=st.form_submit_button("Submit")

    with st.form(key="GetTeacherName"):
        TimeTableDeleteTeacherName_list=[]
        TimeTableDeleteTeacherName= run_query(f'''select distinct teacher_data.teachername from timetable_data 
        inner join teacher_data on timetable_data.tt_lecturename=teacher_data.teacherid 
        where timetable_data.tt_standard="{TimeTableDeleteStandard}" and tt_dayofweek like "{TimeTableWeekDaySelect}"''')
        for names in TimeTableDeleteTeacherName:
            nameslist=names[0]
            TimeTableDeleteTeacherName_list.append(nameslist)
        TimeTableDeleteSelectTeacherName=st.selectbox("Enter Teacher Name",TimeTableDeleteTeacherName_list)
        SubmitTTteachername=st.form_submit_button("Submit")

    with st.form(key="GetLectureName"):
        GetTTLectureName=run_query(f''' select distinct teacher_data.teacherlecture from teacher_Data 
        inner join timetable_Data on timetable_data.tt_lecturename=teacher_data.teacherid 
        where timetable_data.tt_standard="{TimeTableDeleteStandard}" and timetable_Data.tt_dayofweek like "{TimeTableWeekDaySelect}" and teacher_data.teachername like "{TimeTableDeleteSelectTeacherName}"
        ''')
        TTDeleteLectureList=[]
        for lecturenames in GetTTLectureName:
            ttlecture=lecturenames[0]
            TTDeleteLectureList.append(ttlecture)
        SelectTTlecturename=st.selectbox("Enter Lecture Name",TTDeleteLectureList)
        SubmitTTlecturename=st.form_submit_button("Submit")

    with st.form(key="GetTTtime"):
        gettime=run_query(
            f'''
        select timetable_data.tt_fromtime, timetable_data.tt_totime from timetable_data inner join teacher_data on timetable_data.tt_lecturename=teacher_data.teacherid
        where timetable_data.tt_standard=\"{TimeTableDeleteStandard}\" and teacher_data.teacherlecture like \"{SelectTTlecturename}\" and teacher_data.teachername like \"{TimeTableDeleteSelectTeacherName}\" and timetable_Data.tt_Dayofweek like \"{TimeTableWeekDaySelect}\"
        ''')
        timelist=[]
        for times in gettime:
            fromtime=times[0]
            totime=times[1]
            time_join=fromtime+" to "+totime
            timelist.append(time_join)
        TimeForLecture=st.selectbox("Select Time of lecture",timelist)
        SubmitTimeData=st.form_submit_button("Submit")

    if SubmitTimeData:
        if TimeForLecture is not None:
            timesplit=TimeForLecture.split(" to ")
            totimeforquery=timesplit[1]
            fromtimeforquery=timesplit[0]

            run_query("SET FOREIGN_KEY_CHECKS=0")
            run_query(f'''delete t from timetable_data t
                inner join teacher_data e on t.tt_lecturename = e.teacherid 
                where e.TeacherName = \"{TimeTableDeleteSelectTeacherName}\" and t.tt_standard like \"{TimeTableDeleteStandard}\" 
                and t.tt_dayofweek like "{TimeTableWeekDaySelect}"
                and e.teacherlecture like "{SelectTTlecturename}"
                and t.tt_totime like "{totimeforquery}"
                and t.tt_fromtime like "{fromtimeforquery}"
                    ''')
            run_query("SET FOREIGN_KEY_CHECKS=1")
            UserMessage("success",f"Succesfully deleted {SelectTTlecturename} from Time table",3)
        else:
            UserMessage("error","Select a lecture to be deleted",3)
# page_names_to_funcs = {
#     "Add Timetable Data": AddTT,
#     "View Timetable Data": ViewTT,
#     "Delete Timetable Data": DeleteTT,
# }

# selected_page = st.sidebar.radio("Select a page", page_names_to_funcs.keys(),index=0)
# page_names_to_funcs[selected_page]()


SelectedMenuTimeTable =option_menu(
  menu_title="TimeTable",
  menu_icon="list-task",
  options=["Add","View","Delete"],
  icons=["book","book","book"],
  orientation="horizontal"
)


if SelectedMenuTimeTable=="Add":
    AddTT()
elif SelectedMenuTimeTable=="View":
    ViewTT()
elif SelectedMenuTimeTable=="Delete":
    DeleteTT()