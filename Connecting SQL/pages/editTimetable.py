from lib2to3.pytree import convert
from prac import *







with st.form(key="Timetable",clear_on_submit=True):
    input_ttname=st.text_input("Enter Lecture Name")
    col1, col2 = st.columns([1,1])
    with col1:
        start_time=st.time_input("From",datetime.time(8, 45))
    with col2:
        end_time=st.time_input("To",datetime.time(8, 45))
    standard=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
    submit_timetable=st.form_submit_button("Add lecture Data")
    

if submit_timetable:
    if not start_time<end_time:
        st.error("time error")
    else:
        ttname_tokey=run_query(f"select teacherid from teacher_data where teacherlecture = \"{input_ttname}\"")
        for key in ttname_tokey:
            mainkey=key[0]
        run_query(f"Insert into timetable_data(tt_lecturename,tt_fromtime,tt_totime,tt_standard) VALUES ( {mainkey} , \"{start_time}\" , \"{end_time}\" , \"{standard}\")")
        st.success(f"{input_ttname} Added to time table")                                    
     
     