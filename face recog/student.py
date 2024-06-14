from tkinter import BOTH, BOTTOM, END, HORIZONTAL, RIDGE, RIGHT, VERTICAL, W, X, Y, Button, Frame, Label, LabelFrame, StringVar, Tk, messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2
import numpy as np



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x680+0+0")
        self.root.title("face recognition system")
        
        #-----------Variables-------------------
        self.var_dep=StringVar()
        self.var_sub=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_teacher=StringVar()
        
        #bg image
        img1=Image.open(r"C:\Users\acer\Downloads\face recog\face recog\img\bg1.jpg")
        img1=img1.resize((1530,790),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1366,height=790)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT",font=("times new roman",35,"bold"),bg="white",fg="navyblue")
        title_lbl.place(x=0,y=0,width=1366,height=65)
        
        #creating frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=70,width=1366,height=768)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=10,width=660,height=590)
        
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=690,y=10,width=640,height=590)
        
         # current sub info
        current_sub_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current sub Information",font=("verdana",10,"bold"))
        current_sub_frame.place(x=5,y=20,width=640,height=140)
        
        #department label
        dep_label=Label(current_sub_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10)
        #combo box
        dep_combo=ttk.Combobox(current_sub_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CSE","ISE","EC")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        '''
         # course label
        sub_label=Label(current_sub_frame,text="sub",font=("times new roman",13,"bold"))
        sub_label.grid(row=0,column=2,padx=10,sticky=W)
        
        sub_combo=ttk.Combobox(current_sub_frame,textvariable=self.var_sub,font=("times new roman",13,"bold"),state="readonly",width=20)
        sub_combo["values"]=("Select sub","BE","MCA")
        sub_combo.current(0)
        sub_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        '''
        # subject name label
        sub_label=Label(current_sub_frame,text="Subject",font=("times new roman",13,"bold"))
        sub_label.grid(row=0,column=2,padx=10,sticky=W)
        
        sub_combo=ttk.Combobox(current_sub_frame,textvariable=self.var_sub,font=("times new roman",13,"bold"),state="readonly",width=20)
        sub_combo["values"]=("Select Subject","python","DBMS","AIML","CNS")
        sub_combo.current(0)
        sub_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        # year
        year_label=Label(current_sub_frame,text="Year",font=("times new roman",13,"bold"))
        year_label.grid(row=1,column=0,padx=10,pady=15)
        
        year_combo=ttk.Combobox(current_sub_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select year","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=15)
        
        # Semester label
        sem_label=Label(current_sub_frame,text="Semester",font=("times new roman",13,"bold"))
        sem_label.grid(row=1,column=2,padx=10,sticky=W)
        
        sem_combo=ttk.Combobox(current_sub_frame,textvariable=self.var_sem,font=("times new roman",13,"bold"),state="readonly",width=20)
        sem_combo["values"]=("Select Sem","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=15,sticky=W)
        
        # class Student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("verdana",10,"bold"))
        class_student_frame.place(x=5,y=170,width=640,height=390)
        
         #student id
        studentId_label=Label(class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=5,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=18,font=("times new roman",13))
        studentId_entry.grid(row=0,column=1,padx=1,sticky=W)
        
        #student name
        studentname_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        
        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=17,font=("times new roman",13))
        studentname_entry.grid(row=0,column=3,padx=1,pady=5,sticky=W)
        
         #class division 
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=5,pady=15,sticky=W)
        
        #studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=18,font=("times new roman",13))
        #studentId_entry.grid(row=1,column=1,padx=1,pady=15,sticky=W)
        studentId_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
        studentId_combo["values"]=("Select Division","A","B","C")
        studentId_combo.current(0)
        studentId_combo.grid(row=1,column=1,padx=1,pady=15)
        
        #USN
        roll_no_label=Label(class_student_frame,text="USN:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=5,pady=15,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=17,font=("times new roman",13))
        roll_no_entry.grid(row=1,column=3,padx=1,pady=15,sticky=W)
        
        #gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=15,sticky=W)
        
       # gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=18,font=("times new roman",13))
        #gender_entry.grid(row=2,column=1,padx=1,pady=15,sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=1,pady=15,sticky=W)
        
        #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=2,column=2,padx=8,pady=15,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=17,font=("times new roman",13))
        email_entry.grid(row=2,column=3,padx=1,pady=15,sticky=W)
        
        #phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=0,padx=10,pady=15,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=18,font=("times new roman",13))
        phone_entry.grid(row=3,column=1,padx=1,pady=15,sticky=W)
        
         #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=3,column=2,padx=8,pady=15,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=17,font=("times new roman",13))
        teacher_entry.grid(row=3,column=3,padx=1,pady=15,sticky=W)
        
         #radio buttons
        
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo Sample",value="Yes")
        radiobtn1.grid(row=10,column=0,padx=20,pady=20,sticky=W)
        
        #self.var_radio2=StringVar(value="No Photo Sample")
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=10,column=1,padx=20,pady=20,sticky=W)
        
        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=280,width=565,height=35)
        
        save_btn=Button(btn_frame,text="save",command=self.add_data,width=13,font=("times new roman",13,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)
                
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=13,font=("times new roman",13,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=200,y=330,width=200,height=35)
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo sample",width=19,font=("times new roman",13,"bold"),bg="#FFFDD0")
        take_photo_btn.grid(row=0,column=0)
        '''
        update_photo_btn=Button(btn_frame1,text="Update Photo sample",width=33,font=("times new roman",13,"bold"),bg="yellow")
        update_photo_btn.grid(row=0,column=1)
        '''
         #----------------------------------------------------------------------
        # Right Label Frame 
        
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=10,width=650,height=590)
        
         #Searching System in Right Label Frame 
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("verana",11,"bold"),bg="white")
        search_frame.place(x=5,y=20,width=630,height=80)
        
        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="#FFFDD0",fg="black")
        search_label.grid(row=0,column=0,padx=10,sticky=W)
        
        self.var_searchTX=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,font=("times new roman",13,"bold"),state="readonly",width=10)
        search_combo["values"]=("Select","Subject","USN")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.var_search=StringVar()
        Search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=8,pady=5,sticky=W)
        
        search_btn=Button(search_frame,command=self.search_data,text="Search",width=10,font=("times new roman",13,"bold"),bg="green",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=5,padx=4)
        
        # -----------------------------Table Frame-------------------------------------------------
        #table frame
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=130,width=630,height=430)
        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        #create table
        self.student_table=ttk.Treeview(table_frame,columns=("dep","sub","year","sem","id","name","div","usn","gender","email","phone","teach","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("sub",text="Subject")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("usn",text="USN")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("teach",text="Teacher Name")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        #setting width of columns
        self.student_table.column("dep",width=100)
        self.student_table.column("sub",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("usn",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("teach",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor) # type: ignore
        self.fetch_data()
        
    # ==================Function Decleration==============================
        
    def add_data(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)    
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username="root",password="Dee@Reg45",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                    self.var_dep.get(),
                                                                    self.var_sub.get(),
                                                                    self.var_year.get(),
                                                                    self.var_sem.get(),
                                                                    self.var_std_id.get(),
                                                                    self.var_std_name.get(),
                                                                    self.var_div.get(),
                                                                    self.var_roll.get(),
                                                                    self.var_gender.get(), 
                                                                    self.var_email.get(),
                                                                    self.var_phone.get(),
                                                                    self.var_teacher.get(),
                                                                    self.var_radio1.get()
                                                                    
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("sucess","Data Added Sucessfully",parent=self.root)    
            except Exception as ex:   
                messagebox.showerror("error",f"Due to:{str(ex)}",parent=self.root)
     # ===========================Fetch data form database to table ================================
    
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username="root",password="Dee@Reg45",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=tuple(i))
            conn.commit()
        conn.close() 
    #================================get cursor function=======================
   
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]  
                
        self.var_dep.set(data[0])
        self.var_sub.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_teacher.set(data[11])
        self.var_radio1.set(data[12])
    # ========================================Update Function==========================
    
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update",parent=self.root)
                conn=mysql.connector.connect(host="localhost",username="root",password="Dee@Reg45",database="face_recognizer")
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Dee@Reg45",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Subject=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Usn=%s,Gender=%s,Email=%s,Phone=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        
                        self.var_dep.get(),
                        self.var_sub.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    )) 
                    #conn.commit()
                    
                else:
                    if not Update:
                        return
                messagebox.showinfo("Sucess","Update Sucessful",parent=self.root)
                conn.commit()
                self.fetch_data() 
                conn.close()
                
            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)
    
    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student?",parent=self.root)
                conn=mysql.connector.connect(host="localhost",username="root",password="Dee@Reg45",database="face_recognizer")
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Dee@Reg45",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Sucessfully data deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)   
    # Reset Function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_sub.set("Select Subject")
        self.var_year.set("Select year")
        self.var_sem.set("Select Sem")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Divison")    
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")   
     # ===========================Search Data===================
    def search_data(self): 
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='Dee@Reg45',host='localhost',database='face_recognizer')
                my_cursor = conn.cursor()
                sql = "SELECT Dep,Subject,Year,Semester,Student_ID,Name,Division,Gender,Phone,Usn,Email,Teacher,PhotoSample FROM student where Subject='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=tuple(i))
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    #=====================This part is related to Opencv Camera part=======================
    # ==================================Generate Data set take image=========================
    def generate_dataset(self):  
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Dee@Reg45",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Subject=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Usn=%s,Gender=%s,Email=%s,Phone=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        
                        self.var_dep.get(),
                        self.var_sub.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1
                    )) 
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                    
        #load predefined data on face frontals from opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                '''
                def face_croped(img):
                    # convert gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum neighbour 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                '''    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    def face_croped(img):
                    # convert gary sacle
                        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum neighbour 5
                        for (x,y,w,h) in faces:
                            face_croped=img[y:y+h,x:x+w]
                            return face_croped
                    
                    new_face=face_croped(my_frame)
                    # Convert face to a NumPy array
                    new_face_np=np.array(new_face)
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(new_face_np,(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="photos/student."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 
        
                             
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
    
    