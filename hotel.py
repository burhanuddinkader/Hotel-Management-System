
from tkinter import*
from PIL import Image, ImageTk  # pip install pillow
from customer import Cust_Win
from room import RoomBooking

import matplotlib.pyplot as plt
import pandas as pd


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

        details_btn = Button(btn_frame, text="CUSTOMER AUDIT", command=self.cust_audit,  width=22, font=(
            "times new roman", 14, "bold"), bg="black", fg="gold", bd=0,  activeforeground="gold", activebackground="black", cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="COST AUDIT", command=self.cost_audit, width=22, font=(
            "times new roman", 14, "bold"), bg="black", fg="gold", bd=0,  activeforeground="gold", activebackground="black", cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=(
            "times new roman", 14, "bold"), bg="black", fg="gold", bd=0,  command=self.logout, activeforeground="gold", activebackground="black", cursor="hand1")
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

    def logout(self):
        self.root.destroy()

    def cust_audit(self):  # function to go to customer page
        df = pd.read_excel(r"Total.xlsx")
        df.plot(x="Room Type", y="No. of Customers",
                kind="bar", title="Customer Analysis")
        plt.xlabel("Room Type")
        plt.ylabel("No. of Customers")
        plt.show()

    def cost_audit(self):
        df = pd.read_excel(r"Total.xlsx")
        df.plot(x="Room Type", y="Cost", kind="line", title="Cost Analysis")
        plt.xlabel("Room Type")
        plt.ylabel("Cost")
        plt.show()


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
