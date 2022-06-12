from cgitb import text
from email.mime import image
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
from tkinter.tix import IMAGE
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # =========variables=========
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # =====bg image=====
        self.bg = ImageTk.PhotoImage(
            file=r"./Images/register_bg.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # =====left img=====
        self.bg1 = ImageTk.PhotoImage(
            file=r"./Images/register_bg1.jpg")
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
        self.fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last name", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        lname.place(x=370, y=100)
        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        # ------row2-------
        contact = Label(frame, text="Contact No.", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)
        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)
        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # -------row3------
        security_Q = Label(frame, text="Select Security Questions", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=(
            "times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = (
            "Select", "Your Birth Place", "Your Fathers name", "Your School name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)
        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_SecurityA, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        # -----row4------
        password = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        password.place(x=50, y=310)
        self.txt_password = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.txt_password.place(x=50, y=340, width=250)

        confirm_password = Label(frame, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        confirm_password.place(x=370, y=310)
        self.txt_confirm_password = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.txt_confirm_password.place(x=370, y=340, width=250)

        # ======check button======
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable="I Agree the terms and conditions", font=(
            "times new roman", 12, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # =======buttons=======
        img = Image.open(
            r"./Images/register.png")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimg,
                    borderwidth=0, command=self.register_data, cursor="hand2", bg="white")
        b1.place(x=10, y=470, width=300)

        img1 = Image.open(
            r"./Images/login.png")
        img1 = img1.resize((200, 70), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimg1,
                    borderwidth=0, cursor="hand2", bg="white")
        b1.place(x=330, y=470, width=300)

    # ============Function Declaration=============

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


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
