from aiohttp import DataQueue
from  Homepage import *



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
# rows=run_query("Select * from lnames")
# clean_db=pd.DataFrame(rows,columns=["Lecture Names"])
# st.dataframe(clean_db)