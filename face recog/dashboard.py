#from tkinter import *
from tkinter import Button, Label, Tk, Toplevel
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_recog
from attendance import Attendance
from time import strftime

class dashboard:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x680+0+0")
        self.root.title("face recognition system") #Creating 1st window and fixing its geometry area
        
         #bg image
        img1=Image.open(r"C:\Users\acer\Downloads\face recog\face recog\img\bg1.jpg")
        img1=img1.resize((1530,790),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1336,height=790)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="navyblue")
        title_lbl.place(x=-70,y=0,width=1530,height=65)
        
        # time update 
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl=Label(title_lbl,font=("times new roman",18,"bold"),bg="white", fg="black")
        lbl.place(x=80,y=0,width=135, height=50)
        time()


         #student button
        
        std_img_btn=Image.open(r"C:\Users\acer\Downloads\face recog\face recog\img\std1.jpg")
        std_img_btn=std_img_btn.resize((220,220),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)
        
        b1= Button(bg_img,image=self.std_img1,command=self.student_details,cursor="hand2") # type: ignore
        b1.place(x=250,y=100,width=220,height=220)
        b2= Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white") # type: ignore
        b2.place(x=250,y=300,width=220,height=40)
        
        #Detect Face button
        
        det_img_btn=Image.open(r"C:\Users\acer\Downloads\face recog\face recog\img\det1.jpg")
        det_img_btn=det_img_btn.resize((220,220),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)
        
        b3= Button(bg_img,image=self.det_img1,cursor="hand2",command=self.face_data)
        b3.place(x=575,y=100,width=220,height=220)
        b4= Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b4.place(x=575,y=300,width=220,height=40)
        
        #Attendance Face button
        
        att_img_btn=Image.open(r"C:\Users\acer\Downloads\face recog\face recog\img\att.jpg")
        att_img_btn=att_img_btn.resize((220,220),Image.LANCZOS)
        self.photoatt_img_btn=ImageTk.PhotoImage(att_img_btn)
        
        b5= Button(bg_img,image=self.photoatt_img_btn,cursor="hand2",command=self.Attendance)
        b5.place(x=900,y=100,width=220,height=220)
        b6= Button(bg_img,text="Attendance",cursor="hand2",command=self.Attendance,font=("times new roman",15,"bold"),bg="black",fg="white")
        b6.place(x=900,y=300,width=220,height=40)
        
        #Help Support button
        '''
        hlp_img_btn=Image.open(r"C:Users\acerDownloads\face recog\face recogimghlp.jpg")
        hlp_img_btn=hlp_img_btn.resize((220,220),Image.LANCZOS)
        self.photohlp_img_btn=ImageTk.PhotoImage(hlp_img_btn)
        
        b5= Button(bg_img,image=self.photohlp_img_btn,cursor="hand2")
        b5.place(x=1100,y=100,width=220,height=220)
        b6= Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="blue")
        b6.place(x=1100,y=300,width=220,height=40)
        '''
        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
        
        #Train Face button
        
        tra_img_btn=Image.open(r"C:\Users\acer\Downloads\face recog\face recog\img\Traindata.jpg")
        tra_img_btn=tra_img_btn.resize((220,220),Image.LANCZOS)
        self.phototra_img_btn=ImageTk.PhotoImage(tra_img_btn)
        
        b5= Button(bg_img,image=self.phototra_img_btn,cursor="hand2",command=self.train_data)
        b5.place(x=250,y=380,width=220,height=220)
        b6= Button(bg_img,text="Train Data ",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b6.place(x=250,y=580,width=220,height=40)
        
        #Photos Face button
        
        pho_img_btn=Image.open(r"C:\Users\acer\Downloads\face recog\face recog\img\Photos.jpg")
        pho_img_btn=pho_img_btn.resize((220,220),Image.LANCZOS)
        self.photopho_img_btn=ImageTk.PhotoImage(pho_img_btn)
        
        b5= Button(bg_img,image=self.photopho_img_btn,cursor="hand2",command=self.open_img)
        b5.place(x=575,y=380,width=220,height=220)
        
        b6= Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black",fg="white")
        b6.place(x=575,y=580,width=220,height=40)
        
        #Exit Face button
        
        exi_img_btn=Image.open(r"C:\Users\acer\Downloads\face recog\face recog\img\exit.png")
        exi_img_btn=exi_img_btn.resize((220,220),Image.LANCZOS)
        self.photoexi_img_btn=ImageTk.PhotoImage(exi_img_btn)
        
        b5= Button(bg_img,command=self.close,image=self.photoexi_img_btn,cursor="hand2")
        b5.place(x=900,y=380,width=220,height=220)
        
        b6= Button(bg_img,command=self.close,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b6.place(x=900,y=580,width=220,height=40)
        
        # ==================Functions Buttons=====================
       
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def open_img(self):
        os.startfile("photos")
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recog(self.new_window)
        
    def Attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def close(self):
        self.root.destroy()
           
if __name__=="__main__":
    root=Tk()
    obj=dashboard(root)
    root.mainloop()
        