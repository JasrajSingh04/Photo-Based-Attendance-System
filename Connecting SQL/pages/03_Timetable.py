from lib2to3.pytree import convert
from pickle import TRUE
from tracemalloc import start
from pandas import to_datetime

from regex import W
from  Homepage import *










def AddTT():
    with st.form(key="standard_selection"):
        standard_sel=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
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
        time_fromdt_tot=start_time
        time_todt_tot=end_time
        timeistrue=False
        if not start_time<end_time:
            st.error("time error")
        else:
            ttname_tokey=run_query(f"select teacherid from teacher_data where teacherlecture = \"{input_ttname}\" and teachername=\"{input_TeacherName}\"  ")
            for key in ttname_tokey:
                mainkey=key[0]
            time_query=run_query(f"select tt_fromtime , tt_totime from timetable_data where tt_standard=\"{standard_sel}\" and tt_dayofweek=\"{SelectWeekDay}\"")
            check_query=run_query(f"select * from timetable_data where tt_fromtime=\"{start_time}\" or tt_totime=\"{end_time}\" and tt_standard=\"{standard_sel}\"")
            if time_query:
                for time in time_query:
                    time0=datetime.datetime.strptime(time[0], '%H:%M:%S').time()
                    time1=datetime.datetime.strptime(time[1], '%H:%M:%S').time()
                    # if check_query:
                    #     st.error(f"There is Already a lecture from {time[0]} to {time[1]} of condition 1")
                    #     timeistrue=False
                    #     break
                    if (time0<time_fromdt_tot and time1>time_todt_tot):
                        st.error(f"There is Already a lecture from {time[0]} to {time[1]} of condition 2")
                        timeistrue=False
                        break
                    elif time0>time_fromdt_tot and time1<time_todt_tot:
                        st.error(f"There is Already a lecture from {time[0]} to {time[1]} of condition 3")
                        timeistrue=False
                        break
                    elif (time0<time_fromdt_tot or time0<time_todt_tot) and (time1>time_fromdt_tot or time1>time_todt_tot):
                        st.error(f"There is Already a lecture from {time[0]} to {time[1]} of condition 4")
                        timeistrue=False
                        break
                    else:
                        timeistrue=True  
                        pass
            else:
                run_query(f"Insert into timetable_data(tt_lecturename,tt_fromtime,tt_totime,tt_standard,tt_Dayofweek) VALUES ( {mainkey} , \"{start_time}\" , \"{end_time}\" , \"{standard_sel}\" , \"{SelectWeekDay}\")")
                st.success(f"{input_ttname} Added to time table")
                st.success("time query was not none")

            if timeistrue is True:
                if(time0<time_todt_tot and time1<time_todt_tot):
                                run_query(f"Insert into timetable_data(tt_lecturename,tt_fromtime,tt_totime,tt_standard,tt_Dayofweek) VALUES ( {mainkey} , \"{start_time}\" , \"{end_time}\" , \"{standard_sel}\" , \"{SelectWeekDay}\")")
                                st.success(f"{input_ttname} Added to time table condition 1")
                if  (time0>time_fromdt_tot and time1>time_fromdt_tot):
                    run_query(f"Insert into timetable_data(tt_lecturename,tt_fromtime,tt_totime,tt_standard,tt_Dayofweek) VALUES ( {mainkey} , \"{start_time}\" , \"{end_time}\" , \"{standard_sel}\" , \"{SelectWeekDay}\")")
                    st.success(f"{input_ttname} Added to time table condition 2")

     
def ViewTT():
    st.title("View Data")
    with st.form(key="viewTimetableData"):
        input_standard=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
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
    
    



page_names_to_funcs = {
    "Add Timetable Data": AddTT,
    "View Timetable Data": ViewTT,
    "Delete Timetable Data": DeleteTT,
}

selected_page = st.sidebar.radio("Select a page", page_names_to_funcs.keys(),index=0)
page_names_to_funcs[selected_page]()