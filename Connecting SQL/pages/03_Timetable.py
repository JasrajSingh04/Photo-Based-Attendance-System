from lib2to3.pytree import convert
from pickle import TRUE
from tracemalloc import start
from pandas import to_datetime

from regex import W
from  Homepage import *










def main_page():
    with st.form(key="standard_selection"):
        standard_sel=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
        submit_standard_selection=st.form_submit_button("Submit Standard")



    with st.form(key="Timetable",clear_on_submit=True):
        lect_data=run_query(f"select Teacherlecture from teacher_data where teacherstandard=\"{standard_sel}\" ")
        lectureslist=[]
        for lect in lect_data:
            lnamefor=lect[0]
            lectureslist.append(lnamefor)
        input_ttname=st.selectbox("Enter Lecture Name",lectureslist)
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
            ttname_tokey=run_query(f"select teacherid from teacher_data where teacherlecture = \"{input_ttname}\"")
            for key in ttname_tokey:
                mainkey=key[0]
            time_query=run_query(f"select tt_fromtime , tt_totime from timetable_data where tt_standard=\"{standard_sel}\"")
            check_query=run_query(f"select * from timetable_data where tt_fromtime=\"{start_time}\" or tt_totime=\"{end_time}\" and tt_standard=\"{standard_sel}\"")
            if time_query:
                for time in time_query:
                    time0=datetime.datetime.strptime(time[0], '%H:%M:%S').time()
                    time1=datetime.datetime.strptime(time[1], '%H:%M:%S').time()
                    if check_query:
                        st.error(f"There is Already a lecture from {time[0]} to {time[1]} of condition 1")
                        timeistrue=False
                        break
                    elif (time0<time_fromdt_tot and time1>time_todt_tot):
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
                run_query(f"Insert into timetable_data(tt_lecturename,tt_fromtime,tt_totime,tt_standard) VALUES ( {mainkey} , \"{start_time}\" , \"{end_time}\" , \"{standard_sel}\")")
                st.success(f"{input_ttname} Added to time table")
                st.success("time query was not none")

            if timeistrue is True:
                if(time0<time_todt_tot and time1<time_todt_tot):
                                run_query(f"Insert into timetable_data(tt_lecturename,tt_fromtime,tt_totime,tt_standard) VALUES ( {mainkey} , \"{start_time}\" , \"{end_time}\" , \"{standard_sel}\")")
                                st.success(f"{input_ttname} Added to time table condition 1")
                if  (time0>time_fromdt_tot and time1>time_fromdt_tot):
                    run_query(f"Insert into timetable_data(tt_lecturename,tt_fromtime,tt_totime,tt_standard) VALUES ( {mainkey} , \"{start_time}\" , \"{end_time}\" , \"{standard_sel}\")")
                    st.success(f"{input_ttname} Added to time table condition 2")

     
def page2():
    st.title("View Data")
    with st.form(key="viewTimetableData",clear_on_submit=True):
        input_standard=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
        SubmitViewTimetableData=st.form_submit_button("View")
    
    if SubmitViewTimetableData:
      rows=run_query(f'''
    select teacher_data.teacherLecture, timetable_Data.tt_totime,timetable_Data.tt_fromtime,timetable_Data.tt_standard 
    from timetable_data 
    inner join teacher_data on timetable_data.tt_lecturename=teacher_data.teacherid where timetable_data.tt_standard=\"{input_standard}\";
      ''')
      clean_db=pd.DataFrame(rows,columns=["Lecture Name","From","To","Standard"])
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