
from tkinter import Button, Label, Tk, ttk
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime
import csv


class Face_recog:
    def __init__(self,root):
        self.root=root
        self.root.state('zoomed')
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        #self.root.geometry("1366x720+0+0")
        self.root.title("Recognizing Faces")
        self.tagged_faces = set()
        
        #bg image
        img1=Image.open(r"C:\Users\acer\Downloads\face recog\face recog\img\face_recog_bg.jpg")
        img1=img1.resize((1366,750),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1366,height=750)
        
        title_lbl=Label(bg_img,text="FACE  RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=60)
        
        #button
        std_b1 = Button(bg_img,command=self.face_recog,text="Face Recognizer",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1.place(x=600,y=80,width=180,height=45)
    
    #=====================Attendance===================
    '''
    def mark_attendance(self,i,n):
        with open(r"attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0].strip())
                
            if((i not in name_list)) and ((n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{dtString},{d1},Present")
    '''
    def mark_attendance(self, i, n,s):
        file_path = r"C:\Users\acer\Downloads\face recog\face recog\attendance.csv"
        header = ["Student_ID", "Name", "Time", "Date", "Status"]
        
        with open(file_path, "r+", newline="\n") as file:
            # Read existing data
            reader = csv.reader(file)
            my_data_list = list(reader)
            name_list = [entry[0].strip() for entry in my_data_list]

            # Check if the entry already exists
            if (i not in name_list) and (n not in name_list) and (s not in name_list):
                now = datetime.now()
                dt_string = now.strftime("%H:%M:%S")
                date_string = now.strftime("%d/%m/%Y")

                # Append new entry to the data list
                new_entry = [i,n, dt_string, date_string, "Present"]
                my_data_list.append(new_entry)

                # Update the file with the new data
                file.seek(0)
                writer = csv.writer(file)
                if not name_list:
                    # Write header if the file was empty
                    writer.writerow(header)
                writer.writerows(my_data_list) 


            
                
                  
     #=====================face recognition===================
    
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf,minS=(30, 30)):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors,minSize=minS)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),color,1)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host='localhost',username="root",password="Dee@Reg45",database="face_recognizer")
                my_cursor=conn.cursor() 
                
                #my_cursor.execute("select Student_ID from student where Student_ID="+str(id))
                my_cursor.execute("select Student_ID from student where Student_ID=%s",(str(id),))
                i=my_cursor.fetchone()
                #i="+".join(i)
                if i is not None:
                    i_res=map(str,i)
                    i="+".join(i_res)
                else:
                    i="no result"
                #i=str(i).join(i)
                
                my_cursor.execute("select Name from student where Student_ID=%s",(str(id),))
                n=my_cursor.fetchone()
                if n is not None:
                    n_res=map(str,n)
                    n="+".join(n_res)
                else:
                    n="no result"

                #---subject
                my_cursor.execute("select subject from student where Student_ID=%s",(str(id),))
                s=my_cursor.fetchone()
                if s is not None:
                    s_res=map(str,s)
                    s="+".join(s_res)
                else:
                    s="no result"

                    
                if confidence > 77: #77
                    #accuracy_text = f"Accuracy: {confidence}%"
                    cv2.putText(img,f"Student_ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    #cv2.putText(img, accuracy_text, (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(i,n,s)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord
        #----
        def recognize(self,img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img 
        #recog_ins=Face_recog()
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")
        
        videoCap=cv2.VideoCapture(0)
        
        #--------TO MAKE THE VIDEO CAPTURE FULL SCREEN
        # Get the screen resolution
        #screen_width = videoCap.get(cv2.CAP_PROP_FRAME_WIDTH)
        #screen_height = videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        # Set the window to fullscreen
        #cv2.namedWindow("Face Detector", cv2.WND_PROP_FULLSCREEN)
        cv2.namedWindow("Face Detector", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Face Detector", 1200, 650) #width,height
        #cv2.setWindowProperty("Face Detector", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.moveWindow("Face Detector", 0, 0)
        #-------FULL SCREEN code ENDS HERE--
        while True:
            ret,img=videoCap.read()
            img=cv2.flip(img,1) 
            img=recognize(self,img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()
    """
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf, minS=(30, 30)):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors, minSize=minS)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 1)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])

                confidence = int((100 * (1 - predict/300)))

                if confidence > 77 and id not in self.tagged_faces:
                    conn = mysql.connector.connect(host='localhost', username="root", password="Dee@Reg45",
                                                    database="face_recognizer")
                    my_cursor = conn.cursor()

                    my_cursor.execute("select Student_ID from student where Student_ID=%s", (str(id),))
                    i = my_cursor.fetchone()
                    if i is not None:
                        i_res = map(str, i)
                        i = "+".join(i_res)
                    else:
                        i = "no result"

                    my_cursor.execute("select Name from student where Student_ID=%s", (str(id),))
                    n = my_cursor.fetchone()
                    if n is not None:
                        n_res = map(str, n)
                        n = "+".join(n_res)
                    else:
                        n = "no result"

                    my_cursor.execute("select subject from student where Student_ID=%s", (str(id),))
                    s = my_cursor.fetchone()
                    if s is not None:
                        s_res = map(str, s)
                        s = "+".join(s_res)
                    else:
                        s = "no result"

                    cv2.putText(img, f"Student_ID:{i}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Name:{n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(i, n, s)
                    self.tagged_faces.add(id)
                elif confidence <= 77:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

        def recognize(self, img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        videoCap = cv2.VideoCapture(0)

        cv2.namedWindow("Face Detector", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Face Detector", 1200, 650)
        cv2.moveWindow("Face Detector", 0, 0)

        while True:
            ret, img = videoCap.read()
            img = cv2.flip(img, 1)
            img = recognize(self,img, clf, faceCascade)
            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1) == 13:
                break

        videoCap.release()
        cv2.destroyAllWindows()
    """
if __name__=="__main__":
    root=Tk()
    obj=Face_recog(root)
    root.mainloop()



