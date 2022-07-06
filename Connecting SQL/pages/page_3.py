from lib2to3.pytree import convert
from prac import *



with st.form(key="Timetable",clear_on_submit=True):
    input_ttname=st.text_input("Enter Lecture Name")
    col1, col2 = st.columns([1,1])
    with col1:
        start_time=st.time_input("From",datetime.time(8, 45))
    with col2:
        end_time=st.time_input("To",datetime.time(8, 45))
    dayofweek=st.text_input("Day of week")
    submit_timetable=st.form_submit_button("Add lecture Data")
    

if submit_timetable:
    if not start_time<end_time:
        st.error("time error")
    else:
        run_query(f"Insert into timetable_data(tt_lecturename,tt_fromtime,tt_totime,tt_dayofweek) VALUES (\"{input_ttname}\" , \"{start_time}\" , \"{end_time}\" , \"{dayofweek}\")")
        st.success(f"{input_ttname} Added to time table")                                    
     
     
    