from calendar import week, weekday
from datetime import date
from sqlite3 import Date
from tokenize import Number
from unittest import result

from matplotlib.cbook import contiguous_regions
from regex import F
from  Homepage import *




def MyRec(rgb,x,y,w,h,v=20,color=(200,0,0),thikness =2):
    """To draw stylish rectangle around the objects"""
    cv2.line(rgb, (x,y),(x+v,y), color, thikness)
    cv2.line(rgb, (x,y),(x,y+v), color, thikness)

    cv2.line(rgb, (x+w,y),(x+w-v,y), color, thikness)
    cv2.line(rgb, (x+w,y),(x+w,y+v), color, thikness)

    cv2.line(rgb, (x,y+h),(x,y+h-v), color, thikness)
    cv2.line(rgb, (x,y+h),(x+v,y+h), color, thikness)

    cv2.line(rgb, (x+w,y+h),(x+w,y+h-v), color, thikness)
    cv2.line(rgb, (x+w,y+h),(x+w-v,y+h), color, thikness)

def save(img,name, bbox, width=180,height=227):
    x, y, w, h = bbox
    imgCrop = img[y:h, x: w]
    imgCrop = cv2.resize(imgCrop, (width, height))#we need this line to reshape the images
    cv2.imwrite(name+".jpg", imgCrop)

def faces():
    global newdir_lock
    global new_path
    newdir=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    newdir_lock=newdir
    os.mkdir("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/" + newdir)

    detector = dlib.get_frontal_face_detector()
    os.mkdir("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock+"/ImagesForComparison")

    new_path ="D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock+"/ImagesForComparison/Image_"
    # os.mkdir("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir+"/ImagesForComparison")
    facesCounter=0
    for imagesVerifiedCounter , verifiedImages in enumerate(attendence_file):
        file_bytes = np.asarray(bytearray(verifiedImages.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)  
        frame =opencv_image
        gray = frame
        faces = detector(gray)
        fit =20
        # detect the face
        for face in faces:
            x1, y1 = face.left(), face.top()
            x2, y2 = face.right(), face.bottom()
            cv2.rectangle(frame,(x1,y1),(x2,y2),(220,255,220),1)
            MyRec(frame, x1, y1, x2 - x1, y2 - y1, 10, (0,250,0), 3)
            # save(gray,new_path+str(counter),(x1-fit,y1-fit,x2+fit,y2+fit))
            save(gray,new_path+str(facesCounter),(x1,y1,x2,y2))
            facesCounter+=1
        frame = cv2.resize(frame,(800,800))
        cv2.imwrite("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock+"/img_"+str(imagesVerifiedCounter)+".jpg",frame)
    

def verify_faces():
    global newdir_lock_main
    global new_path_main
    global NumberOfFaces
    NumberOfFaces=0
    newdir=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    newdir_lock_main=newdir
    os.mkdir("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/" + newdir)
    detector = dlib.get_frontal_face_detector()
    new_path_main ="D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock_main+"/Image_"
    for No_of_files,Uploaded_files in enumerate(attendence_file):
        file_bytes = np.asarray(bytearray(Uploaded_files.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)  
        frame =opencv_image
        gray = frame
        faces = detector(gray)
        fit =20
        # detect the face
        for face in faces:
            x1, y1 = face.left(), face.top()
            x2, y2 = face.right(), face.bottom()
            cv2.rectangle(frame,(x1,y1),(x2,y2),(220,255,220),1)
            MyRec(frame, x1, y1, x2 - x1, y2 - y1, 10, (0,250,0), 3)
            NumberOfFaces=NumberOfFaces+1
        No_of_files+=1
        frame = cv2.resize(frame,(800,800))
        cv2.imwrite("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock_main+"/"+str(No_of_files)+".jpg",frame)
        



    
image1=None


# teacher_name=run_query("Select teachername from teacher_data")
# tnamelist=[]
# for teacher in teacher_name:
#     tnamefor=teacher[0]
#     tnamelist.append(tnamefor)


with st.form(key="getstandard",clear_on_submit=False):
    studentstandard=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
    date_in=st.date_input("Select Attendence Date",datetime.date.today())
    submit_standard=st.form_submit_button("Enter standard")
    

with st.form(key="getlecture",clear_on_submit=False):
    date_inborn = date_in.strftime("%A")
    st.write(f"Day of the week is {date_inborn} ")
    lecture_name=run_query(f"select distinct teacher_data.teacherlecture from timetable_data inner join teacher_data on timetable_data.tt_lecturename=teacher_data.teacherid where timetable_data.tt_standard=\"{studentstandard}\" and tt_dayofweek like \"{date_inborn}\"")
    lnamelist=[]
    for lectures in lecture_name:
        lnamefor=lectures[0]
        lnamelist.append(lnamefor)
    lecture_name=st.selectbox("Enter lecture name",lnamelist)
    submit_button_for_teacher_name=st.form_submit_button("Submit")


with st.form(key="GetTeacher",clear_on_submit=False):
    TeacherNameForList=run_query(f"select distinct teacher_data.teachername from timetable_data inner join teacher_data on timetable_data.tt_lecturename=teacher_data.teacherid where timetable_data.tt_standard=\"{studentstandard}\" and teacher_data.teacherlecture like \"{lecture_name}\"")
    tnamelist=[]
    for tnames in TeacherNameForList:
        tnamefor=tnames[0]
        tnamelist.append(tnamefor)
    TeacherNameAttendence=st.selectbox("Select Teacher Name",tnamelist)
    submit_getTeacher=st.form_submit_button("Submit")

with st.form(key="keytimings",clear_on_submit=False):
    gettime=run_query(
        f'''
    select  timetable_data.tt_fromtime, timetable_data.tt_totime from timetable_data inner join teacher_data on timetable_data.tt_lecturename=teacher_data.teacherid
    where timetable_data.tt_standard=\"{studentstandard}\" and teacher_data.teacherlecture like \"{lecture_name}\" and teacher_data.teachername like \"{TeacherNameAttendence}\" and timetable_Data.tt_Dayofweek like \"{date_inborn}\"
'''
    )
    timelist=[]
    for times in gettime:
        fromtime=times[0]
        totime=times[1]
        time_join=fromtime+" to "+totime
        timelist.append(time_join)
    
    TimeForLecture=st.selectbox("Select Time of lecture",timelist)
    attendence_file = st.file_uploader(label = "Upload file", type=["jpg","png","jfif"],accept_multiple_files=True)
    submit_button=st.form_submit_button("Attendence")


if submit_button:
    imageslist=[]
    if attendence_file is not None:
        verify_faces()
        for imagesInFolder in glob.glob("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock_main+"/*.jpg"):
            image1=Image.open(imagesInFolder)
            imageslist.append(image1)
            
    else:
        UserMessage("error","Add a photo",3)




with st.form(key="Verifypicture"):
    if image1 is not None:
        wait = None
        for items in imageslist:
            st.image(items)
        st.write(f"Total of {NumberOfFaces} faces got detected \nIf Less faces got detected reclick the picture")    
    else:
        wait = st.write("...Waiting for image")
    col1, col2 = st.columns([1,1])
    with col1:
        submitverifypicture=st.form_submit_button("Verify")
    with col2:
        notverify=st.form_submit_button("Disapprove")





if submitverifypicture and attendence_file is None:
    UserMessage("error","Fill all the fields",3)

if notverify:
    UserMessage("error","Photo not verified",3)





 

if submitverifypicture and attendence_file is not None:
    faces()
    timesplit=TimeForLecture.split(" to ")
    totimeforquery=timesplit[1]
    fromtimeforquery=timesplit[0]

    print(timesplit)
    

    tname = run_query(f'''select teacher_data.teacherid from timetable_data inner join teacher_data on timetable_data.tt_lecturename=teacher_data.teacherid 
    where teacher_data.teacherstandard like \"{studentstandard}\" 
    and teacher_data.teachername like \"{TeacherNameAttendence}\" 
    and teacher_data.teacherlecture like \"{lecture_name}\" 

    ''')
    
    lectureid=run_query(f'''select timetable_data.tt_id from timetable_data 
    inner join teacher_data on timetable_data.tt_lecturename=teacher_data.teacherid 
    where teacher_data.teacherid={tname[0][0]}
    and timetable_data.tt_totime=\"{totimeforquery}\" 
    and  timetable_Data.tt_fromtime=\"{fromtimeforquery}\" 
    and timetable_data.tt_dayofweek like \"{date_inborn}\"
    ''')
    
    photo_data=run_query(f"select photourl from student_data where studentstandard= \"{studentstandard}\"")

    if not photo_data:
      UserMessage("error","There are no students information available in the class",3)
      st.stop()
    
    with st.spinner("Wait for it.It may take up to 2 minutes depending upon the number of students"):
        for data in photo_data:
            try:
                if resultmain["verified"] is False:
                    run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( {studentid[0][0]} , {tname[0][0]}, {lectureid[0][0]} , \"absent\", \"{date_in}\" )")
            except:
                pass                                                                                           
            for img in glob.glob("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock+"/ImagesForComparison/*.jpg"):
                image_link=data[0]
                ImageOfAttendece=cv2.imread(img)
                ImageOfDatabase=cv2.imread(image_link)
                resultmain=DeepFace.verify(ImageOfAttendece,ImageOfDatabase,model_name="Facenet", enforce_detection=False,detector_backend="mtcnn")
                studentid=run_query(f"select studentid from student_data where photourl = \"{image_link}\"")
            
                if resultmain["verified"] is True:
                    print(resultmain["verified"])
                    run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( {studentid[0][0]} , {tname[0][0]}, {lectureid[0][0]} , \"present\", \"{date_in}\" )")
                    
                    break
        time.sleep(0.5)

    if resultmain["verified"] is False:
                run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( {studentid[0][0]} , {tname[0][0]}, {lectureid[0][0]} , \"absent\", \"{date_in}\" )")

    UserMessage("success",f"Attendence Successfully created for {studentstandard} for date {date_in}",5)





































# if submitverifypicture and attendence_file is not None:
#     faces()
#     tname = run_query(f"select teacher_data.teacherid from timetable_data inner join teacher_data on timetable_data.tt_lecturename=teacher_data.teacherid where timetable_data.tt_standard=\"{studentstandard}\"")
#     for teacher in tname:
#         teacher = teacher[0]
#     lectureid=run_query(f"select timetable_data.tt_id from timetable_data inner join teacher_data on timetable_data.tt_lecturename=teacher_data.teacherid where teacher_data.teacherid={teacher}")

#     photo_data=run_query(f"select photourl from student_data where studentstandard= \"{studentstandard}\"")
#     for data in photo_data:
#         try:
#             if resultmain["verified"] is False:
#                 run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( {studentid[0][0]} , {teacher}, {lectureid[0][0]} , \"absent\", \"{date_in}\" )")
#         except:
#             pass
        
#         for img in glob.glob("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock+"/*.jpg"):
#             image_link=data[0]
#             ImageOfAttendece=cv2.imread(img)
#             ImageOfDatabase=cv2.imread(image_link)
#             resultmain=DeepFace.verify(ImageOfAttendece,ImageOfDatabase,model_name="Facenet", enforce_detection=False,detector_backend="mtcnn")
#             studentid=run_query(f"select studentid from student_data where photourl = \"{image_link}\"")
        
#             if resultmain["verified"] is True:
                
#                 print(resultmain["verified"])
#                 run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( {studentid[0][0]} , {teacher}, {lectureid[0][0]} , \"present\", \"{date_in}\" )")
#                 break
            
#     if resultmain["verified"] is False:
#                 run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( {studentid[0][0]} , {teacher}, {lectureid[0][0]} , \"absent\", \"{date_in}\" )")

            
#             # stuname=run_query(f"select studentname from student_data where photourl like \" {image_link} \" ")
#             # if resultmain["verified"] is True:
#             #     run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( \"{image_link}\" , \"{tname}\", \"{lecture_name}\" , \"present\", \"{date_in}\" )")
#             #     break
#             # else:
#             #      run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( \"{image_link}\" , \"{tname}\", \"{lecture_name}\" , \"absent\", \"{date_in}\" )")
#     print("completed loop")
#     st.success("added data")
#     # run_query(f"UPDATE student_ca  SET `{locktime}`=COALESCE(`{locktime}`,\"absent\");")
#     # sql_query = pd.read_sql_query('''
#     #                         select * from student_ca
#     #                         '''
#     #                         ,mydb)
#     # df=pd.DataFrame(sql_query)
#     # df.to_csv(fr"{new_path}+{locktime}+.csv",index=False)
#     # print("done")
#     # run_query(f"alter table student_ca drop column `{locktime}`")


# if submitverifypicture:
#     st.error("Fll all the fields")























# def MyRec(rgb,x,y,w,h,v=20,color=(200,0,0),thikness =200):
#     """To draw stylish rectangle around the objects"""
#     cv2.line(rgb, (x,y),(x+v,y), color, thikness)
#     cv2.line(rgb, (x,y),(x,y+v), color, thikness)

#     cv2.line(rgb, (x+w,y),(x+w-v,y), color, thikness)
#     cv2.line(rgb, (x+w,y),(x+w,y+v), color, thikness)

#     cv2.line(rgb, (x,y+h),(x,y+h-v), color, thikness)
#     cv2.line(rgb, (x,y+h),(x+v,y+h), color, thikness)

#     cv2.line(rgb, (x+w,y+h),(x+w,y+h-v), color, thikness)
#     cv2.line(rgb, (x+w,y+h),(x+w-v,y+h), color, thikness)

# def save(img,name, bbox, width=180,height=227):
#     x, y, w, h = bbox
#     imgCrop = img[y:h, x: w]
#     imgCrop = cv2.resize(imgCrop, (width, height))#we need this line to reshape the images
#     cv2.imwrite(name+".jpg", imgCrop)

# def faces():
#     global newdir_lock
#     global new_path
#     newdir=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#     newdir_lock=newdir
#     os.mkdir("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/" + newdir)
    
#     detector = dlib.get_frontal_face_detector()
#     new_path ="D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock+"/Image_"
#     file_bytes = np.asarray(bytearray(attendence_file.read()), dtype=np.uint8)
#     opencv_image = cv2.imdecode(file_bytes, 1)  
#     frame =opencv_image
#     gray = frame
#     faces = detector(gray)
#     fit =20
#     # detect the face
#     for counter,face in enumerate(faces):
#         print(counter)
#         x1, y1 = face.left(), face.top()
#         x2, y2 = face.right(), face.bottom()
#         cv2.rectangle(frame,(x1,y1),(x2,y2),(220,255,220),1)
#         MyRec(frame, x1, y1, x2 - x1, y2 - y1, 10, (0,250,0), 3)
#         # save(gray,new_path+str(counter),(x1-fit,y1-fit,x2+fit,y2+fit))
#         save(gray,new_path+str(counter),(x1,y1,x2,y2))
#     frame = cv2.resize(frame,(800,800))
#     cv2.imshow("im1",frame) 
#     cv2.waitKey(0)  
#     print("done saving")




# teacher_name=run_query("Select teachername from teacher_data")
# tnamelist=[]
# for teacher in teacher_name:
#     tnamefor=teacher[0]
#     tnamelist.append(tnamefor)


# lecture_name=run_query("select tt_lecturename from timetable_data")
# lnamelist=[]
# for lectures in lecture_name:
#     lnamefor=lectures[0]
#     lnamelist.append(lnamefor)


# with st.form(key="GetAttendence",clear_on_submit=True):
#     date=st.date_input("Select Attendence Date",datetime.date.today())
#     tname=st.selectbox("Enter teacher name ",tnamelist)
#     lecture_name=st.selectbox("Enter lecture name",lnamelist)
#     attendence_file = st.file_uploader(label = "Upload file", type=["jpg","png","jfif"])
#     submit_button=st.form_submit_button("Attendence")
    

# if submit_button:
#     if attendence_file is not None:
#         faces()
#         st.success("done saving")
#         time = datetime.datetime.now().strftime('%Y-%m-%d')
#         locktime=time
#         run_query(f"alter table student_ca ADD COLUMN `{locktime}` varchar(255);")
#         photo_data=run_query("select photourl from student_ca where P{")
#         for data in photo_data:
#             image_link=data[0]
#             for img in glob.glob("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock+"/*.jpg"):
#                 ImageOfAttendece=cv2.imread(img)
#                 ImageOfDatabase=cv2.imread(image_link)
#                 resultmain=DeepFace.verify(ImageOfAttendece,ImageOfDatabase,model_name="Facenet", enforce_detection=False,detector_backend="mtcnn")
#                 if resultmain["verified"] is True:
#                     run_query(f"update student_ca set `{locktime}` = \"present\" where photo_link=\"{image_link}\" ")
#                     break 
#         print("completed loop")
#         run_query(f"UPDATE student_ca  SET `{locktime}`=COALESCE(`{locktime}`,\"absent\");")
#         sql_query = pd.read_sql_query('''
#                                 select * from student_ca
#                                 '''
#                                 ,mydb)
#         df=pd.DataFrame(sql_query)
#         df.to_csv(fr"{new_path}+{locktime}+.csv",index=False)
#         print("done")
#         run_query(f"alter table student_ca drop column `{locktime}`")

























