from sqlite3 import Date
from unittest import result

from matplotlib.cbook import contiguous_regions
from regex import F
from prac import *

















def MyRec(rgb,x,y,w,h,v=20,color=(200,0,0),thikness =200):
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
    new_path ="D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock+"/Image_"
    file_bytes = np.asarray(bytearray(attendence_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)  
    frame =opencv_image
    gray = frame
    faces = detector(gray)
    fit =20
    # detect the face
    for counter,face in enumerate(faces):
        print(counter)
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()
        cv2.rectangle(frame,(x1,y1),(x2,y2),(220,255,220),1)
        MyRec(frame, x1, y1, x2 - x1, y2 - y1, 10, (0,250,0), 3)
        # save(gray,new_path+str(counter),(x1-fit,y1-fit,x2+fit,y2+fit))
        save(gray,new_path+str(counter),(x1,y1,x2,y2))
    frame = cv2.resize(frame,(800,800))
    cv2.imshow("im1",frame) 
    cv2.waitKey(0)  
    print("done saving")




teacher_name=run_query("Select teachername from teacher_data")
tnamelist=[]
for teacher in teacher_name:
    tnamefor=teacher[0]
    tnamelist.append(tnamefor)


lecture_name=run_query("select tt_lecturename from timetable_data")
lnamelist=[]
for lectures in lecture_name:
    lnamefor=lectures[0]
    lnamelist.append(lnamefor)




with st.form(key="GetAttendence",clear_on_submit=True):
    date_in=st.date_input("Select Attendence Date",datetime.date.today())
    studentstandard=st.selectbox("Enter Standard",["FYIT","SYIT","TYIT"])
    tname=st.selectbox("Enter teacher name ",tnamelist)
    lecture_name=st.selectbox("Enter lecture name",lnamelist)
    attendence_file = st.file_uploader(label = "Upload file", type=["jpg","png","jfif"])
    submit_button=st.form_submit_button("Attendence")
    

if submit_button:
    if attendence_file is not None:
        faces()
        st.success("done saving")
        # time = datetime.datetime.now().strftime('%Y-%m-%d')
        # locktime=time
        # run_query(f"alter table student_ca ADD COLUMN `{locktime}` varchar(255);")
        
        photo_data=run_query(f"select photourl from student_data where studentstandard= \"{studentstandard}\"")
        for data in photo_data:
            try:
                if resultmain["verified"] is False:
                    run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( \"{image_link}\" , \"{tname}\", \"{lecture_name}\" , \"absent\", \"{date_in}\" )")
            except:
                pass
            # try:
            #     if resultmain["verified"] is True:
            #             run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( \"{image_link}\" , \"{tname}\", \"{lecture_name}\" , \"present\", \"{date_in}\" )")
            #     if resultmain["verified"] is False:
            #             run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( \"{image_link}\" , \"{tname}\", \"{lecture_name}\" , \"absent\", \"{date_in}\" )")        
            # except:
                # pass
            for img in glob.glob("D:/3rd Year Project/3rd-year-project/Connecting SQL/current attendence imaage/"+newdir_lock+"/*.jpg"):
                image_link=data[0]
                ImageOfAttendece=cv2.imread(img)
                ImageOfDatabase=cv2.imread(image_link)
                resultmain=DeepFace.verify(ImageOfAttendece,ImageOfDatabase,model_name="Facenet", enforce_detection=False,detector_backend="mtcnn")
                print("       dasdasd                      ")
                print("           asdasdasd                  ")
                if resultmain["verified"] is True:
                    print(resultmain["verified"])
                    run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( \"{image_link}\" , \"{tname}\", \"{lecture_name}\" , \"present\", \"{date_in}\" )")
                    break
                
        if resultmain["verified"] is False:
                    run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( \"{image_link}\" , \"{tname}\", \"{lecture_name}\" , \"absent\", \"{date_in}\" )")

                
                # stuname=run_query(f"select studentname from student_data where photourl like \" {image_link} \" ")
                # if resultmain["verified"] is True:
                #     run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( \"{image_link}\" , \"{tname}\", \"{lecture_name}\" , \"present\", \"{date_in}\" )")
                #     break
                # else:
                #      run_query(f"insert into attendence_data(att_studentid,att_teacherid,att_timetableid,ispresent,dateoflecture) VALUES ( \"{image_link}\" , \"{tname}\", \"{lecture_name}\" , \"absent\", \"{date_in}\" )")
        print("completed loop")
        st.success("added data")
        # run_query(f"UPDATE student_ca  SET `{locktime}`=COALESCE(`{locktime}`,\"absent\");")
        # sql_query = pd.read_sql_query('''
        #                         select * from student_ca
        #                         '''
        #                         ,mydb)
        # df=pd.DataFrame(sql_query)
        # df.to_csv(fr"{new_path}+{locktime}+.csv",index=False)
        # print("done")
        # run_query(f"alter table student_ca drop column `{locktime}`")














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

























