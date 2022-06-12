from __future__ import nested_scopes
from cgitb import text
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from email import message
from tkinter import ttk
from tkinter import messagebox
import random
import mysql.connector
from customer import Cust_Win
from room import RoomBooking


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        # Background image pura bg cover nahi kar raha.....
        self.bg = ImageTk.PhotoImage(
            file=r"C:\Users\Vardhan\Desktop\python mini proj\Hotel-Management-System\Images\register_bg1.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        self.bg = ImageTk.PhotoImage(
            file=r'C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\register_bg.jpg')
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, width=1530, height=790)

        frame = Frame(self.root, bg='white')
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(
            r"C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\register_bg1.jpg")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text='Get Started', font=(
            'times new roman', 20, 'bold'), bg='white', fg='black')
        get_str.place(x=95, y=100)

        # label
        username = Label(frame, text='Email', font=(
            'times new roman', 15, 'bold'), bg='white', fg='black')
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=('times new roman', 15, 'bold'))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text='Password', font=(
            'times new roman', 15, 'bold'), bg='white', fg='black')
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=('times new roman', 15, 'bold'))
        self.txtpass.place(x=40, y=250, width=270)

        # Icon Imgaes
        img2 = Image.open(
            r"C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\login_logo.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="white", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(
            r"C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\login_icon.jpg")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="white", borderwidth=0)
        lblimg3.place(x=650, y=395, width=25, height=25)

        # Button
        loginbtn = Button(frame, text='Login', command=self.login, font=('times new roman', 15, 'bold'),
                          width=13, bg='red', fg='black', activeforeground="black", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn = Button(frame, text='New User Register', command=self.register_window, borderwidth=0, font=(
            'times new roman', 12, 'bold'), width=13, bg='white', fg='black', activeforeground="black", activebackground="white")
        registerbtn.place(x=20, y=350, width=160)

        forgetbtn = Button(frame, text='Forget Password', command=self.forgot_password_window, borderwidth=0, font=(
            'times new roman', 12, 'bold'), width=13, bg='white', fg='black', activeforeground="black", activebackground="white")
        forgetbtn.place(x=10, y=380, width=160)

    # Isme inbuilt prompts diye hai so dekh lena

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "all field required")
        elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("Success", "Welcome to codewithkiran channel")

        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="@Vardhan27", database="hotel_management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))

            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # =====bg image=====
        self.bg = ImageTk.PhotoImage(
            file=r"C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\register_bg.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # =====left img=====
        self.bg1 = ImageTk.PhotoImage(
            file=r"C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\register_bg1.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # =====main frame=====
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="red", bg="white")
        register_lbl.place(x=20, y=20)

        # =====labels and entries=====

        # -----row1-------
        fname = Label(frame, text="First name", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        fname.place(x=50, y=100)
        fname_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last name", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        lname.place(x=370, y=100)
        self.txt_lname = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        # ------row2-------
        contact = Label(frame, text="Contact No.", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)
        self.txt_contact = ttk.Entry(
            frame, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)
        self.txt_email = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # -------row3------
        security_Q = Label(frame, text="Select Security Questions", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame, font=(
            "times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = (
            "Select", "Your Birth Place", "Your Fathers name", "Your School name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)
        self.txt_security = ttk.Entry(
            frame, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        # -----row4------
        password = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        password.place(x=50, y=310)
        self.txt_password = ttk.Entry(
            frame, font=("times new roman", 15, "bold"))
        self.txt_password.place(x=50, y=340, width=250)

        confirm_password = Label(frame, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        confirm_password.place(x=370, y=310)
        self.txt_confirm_password = ttk.Entry(
            frame, font=("times new roman", 15, "bold"))
        self.txt_confirm_password.place(x=370, y=340, width=250)

        # ======check button======
        checkbtn = Checkbutton(frame, text="I Agree the terms and conditions", font=(
            "times new roman", 12, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # =======buttons=======
        img = Image.open(
            r"C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\register.png")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimg,
                    borderwidth=0, cursor="hand2", bg="white")
        b1.place(x=10, y=470, width=300)

        img1 = Image.open(
            r"C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\login.png")
        img1 = img1.resize((200, 70), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimg1,
                    borderwidth=0, cursor="hand2", bg="white")
        b1.place(x=330, y=470, width=300)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password didn't match")
        # elif self.var_check.get() == 0:
        #     messagebox.showerror(
        #         "Error", "Please agree to our terms and condition")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="@Vardhan27", database="hotel_management")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exist")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_SecurityA.get(),
                    self.var_pass.get()

                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered Successfully")

    def return_login(self):
        self.root.destroy()


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        # (+0+0) means starting from x=0,y=0
        self.root.geometry("1550x800+0+0")
        # root.attributes('-fullscreen', True)  #To make it fullscreen

        # ======1st Image======
        img1 = Image.open(
            r"C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\hotel1.jpg")
        img1 = img1.resize((1550, 140), Image.ANTIALIAS)  # Antialias is imp
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbling = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lbling.place(x=0, y=0, width=1550, height=140)

        # ======logo======
        img2 = Image.open(
            r"C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\logo.jpg")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)  # Antialias is imp
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbling = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbling.place(x=0, y=0, width=230, height=140)

        # ======Title======
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=(
            "times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # ======In Frame======
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # ======Menu======
        lbl_title = Label(main_frame, text="MENU", font=(
            "times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=230)

        # ======btn Frame======
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=(
            "times new roman", 14, "bold"), bg="black", fg="gold", bd=0, activeforeground="gold", activebackground="black", cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.room_details, width=22, font=(
            "times new roman", 14, "bold"), bg="black", fg="gold", bd=0,  activeforeground="gold", activebackground="black", cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="CUSTOMER AUDIT",  width=22, font=(
            "times new roman", 14, "bold"), bg="black", fg="gold", bd=0,  activeforeground="gold", activebackground="black", cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="COST AUDIT",  width=22, font=(
            "times new roman", 14, "bold"), bg="black", fg="gold", bd=0,  activeforeground="gold", activebackground="black", cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=(
            "times new roman", 14, "bold"), bg="black", fg="gold", bd=0,  activeforeground="gold", activebackground="black", cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

        # ======Right side image======
        img3 = Image.open(
            r"C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\cabin.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)  # Antialias is imp
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbling1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lbling1.place(x=225, y=0, width=1310, height=590)

        # ======Down image======
        img4 = Image.open(
            r"C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\hotel2.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)  # Antialias is imp
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbling2 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lbling2.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(
            r"C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\khana.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)  # Antialias is imp
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lbling3 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lbling3.place(x=0, y=420, width=230, height=190)

    def cust_details(self):  # function to go to customer page
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def room_details(self):  # function to go to customer page
        self.new_window = Toplevel(self.root)
        self.app = RoomBooking(self.new_window)

    # def cust_audit(self):  # function to go to customer page
    #     df=pd.read_excel(r"Total.xlsx")
    #     df.plot(x="Room Type", y="No. of Customers", kind="bar", title="Customer Analysis")
    #     plt.xlabel("Room Type")
    #     plt.ylabel("No. of Customers")
    #     plt.show()

    # def cost_audit(self):
    #     df=pd.read_excel(r"Total.xlsx")
    #     df.plot(x="Room Type", y="Cost", kind="line", title="Cost Analysis")
    #     plt.xlabel("Room Type")
    #     plt.ylabel("Cost")
    #     plt.show()


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
