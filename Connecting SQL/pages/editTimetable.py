from lib2to3.pytree import convert

from regex import W
from prac import *











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
    if not start_time<end_time:
        st.error("time error")
    else:
        ttname_tokey=run_query(f"select teacherid from teacher_data where teacherlecture = \"{input_ttname}\"")
        for key in ttname_tokey:
            mainkey=key[0]
        run_query(f"Insert into timetable_data(tt_lecturename,tt_fromtime,tt_totime,tt_standard) VALUES ( {mainkey} , \"{start_time}\" , \"{end_time}\" , \"{standard_sel}\")")
        st.success(f"{input_ttname} Added to time table")                                    
    
     