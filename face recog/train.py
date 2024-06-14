from tkinter import Button, Label, Tk, ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
import cv2
import cv2.face
#from cv2 import face

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x680+0+0")
        self.root.title("Training data")
        
         #bg image
        img1=Image.open(r"C:\Users\acer\Downloads\face recog\face recog\img\train_img.jpg")
        img1=img1.resize((1366,750),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1366,height=750)
        
        title_lbl=Label(bg_img,text="TRAINING  DATASET",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=60)
        
        # Training button 1
        # std_img_btn=Image.open(r"C:\Users\acer\Downloads\face recog\face recog\img\t_btn1.png")
        # std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        # self.std_img1=ImageTk.PhotoImage(std_img_btn)

        # std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        # std_b1.place(x=600,y=70,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="TRAIN DATASET",cursor="hand2",font=("tahoma",15,"bold"),bg="green",fg="white")
        std_b1_1.place(x=410,y=410,width=180,height=45)
        
        #training Functions
    def train_classifier(self):
        data_dir=(r"C:\Users\acer\Downloads\face recog\face recog\photos")
        imagepath=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in imagepath:
            img=Image.open(image).convert('L') #convert to gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[-1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            #cap.release()
            #cv2.destroyAllWindows()
        
        ids=np.array(ids)
        
        #training Classifier
        
        #clf=cv2.face.LBPHFaceRecognizer_create()
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write(r"classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success","Training datasets Completed!",parent=self.root)
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()        