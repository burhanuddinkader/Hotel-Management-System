from email import message
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PIL import Image,ImageTk   #pip install pillow

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Background image pura bg cover nahi kar raha.....  
        self.bg=ImageTk.PhotoImage(file=r"C:\Desktop\Images\login_back.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Desktop\Images\login_logo.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)  #Antialias is imp
        self.photoimage1=ImageTk.PhotoImage(img1)

        lbling1=Label(self.root,image=self.photoimage1,bg="black",borderwidth=0)
        lbling1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #======icon image=======
        img2=Image.open("C:\Desktop\Images\login_logo.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)  #Antialias is imp
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbling1=Label(self.root,image=self.photoimage2,bg="black",borderwidth=0)
        lbling1.place(x=650,y=323,width=25,height=25)

        img3=Image.open("C:\Desktop\Images\login_icon.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)  #Antialias is imp
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbling1=Label(self.root,image=self.photoimage3,bg="black",borderwidth=0)
        lbling1.place(x=650,y=395,width=25,height=25)

        #LoginButton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#FFA500",activeforeground="white",activebackground="#FFA500")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #RegisterButton
        loginbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=15,y=350,width=160)

        #forgetpassbtn
        loginbtn=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=10,y=370,width=160)
    
    # Isme inbuilt prompts diye hai so dekh lena 
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to codewithkiran channel")
        else:
            messagebox.showerror("Invalid","Invalid username&password")    

                




if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()