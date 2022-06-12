from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
# hello


class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # =====variables=====
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # ======Title======
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=(
            "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ======logo======
        img2 = Image.open(
            r"C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\logo.jpg")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)  # Antialias is imp
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbling = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbling.place(x=5, y=2, width=100, height=40)

        # ======labelFrame======
        labelframeleft = LabelFrame(
            self.root, bd=2, relief=RIDGE, text="Room Booking Details", font=("arial", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ======labels and entries======
        # cust Contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, font=(
            "arial", 13, "bold"), width=20)
        enty_contact.grid(row=0, column=1, sticky=W)

        # Fetch Data Button
        btnFetchData = Button(labelframeleft, command=self.Fetch_contact, text="Fetch Data", font=(
            "arial", 8, "bold"), bg="black", fg="gold", width=8)
        btnFetchData.place(x=347, y=4)

        # Check-in-Date
        check_in_date = Label(labelframeleft, text="Check-in Date:",
                              font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date = ttk.Entry(
            labelframeleft, textvariable=self.var_checkin, font=("arial", 13, "bold"), width=29)
        txtcheck_in_date.grid(row=1, column=1)

        # Check-out-Date
        check_out_date = Label(
            labelframeleft, text="Check-out Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)
        txtcheck_out_date = ttk.Entry(
            labelframeleft, textvariable=self.var_checkout, font=("arial", 13, "bold"), width=29)
        txtcheck_out_date.grid(row=2, column=1)

        # Room Type
        label_RoomType = Label(labelframeleft, text="Room Type:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)
        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=(
            "arial", 12, "bold"), width=27, state="readonly")
        combo_RoomType["value"] = ("Single", "Double", "Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable = Label(labelframeleft, text="Rooms Available:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        txtRoomAvailable = ttk.Entry(
            labelframeleft, textvariable=self.var_roomavailable, font=("arial", 13, "bold"), width=29)
        txtRoomAvailable.grid(row=4, column=1)

        # Meal
        lblMeal = Label(labelframeleft, text="Meal:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal = ttk.Entry(labelframeleft, textvariable=self.var_meal, font=(
            "arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # No of Days
        lblNoOfDays = Label(labelframeleft, text="No. of Days:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_noofdays, font=(
            "arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblPaidTax = Label(labelframeleft, text="Paid Tax:",
                           font=("arial", 12, "bold"), padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)
        txtPaidTax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, font=(
            "arial", 13, "bold"), width=29)
        txtPaidTax.grid(row=7, column=1)

        # Sub Total
        lblSubTotal = Label(labelframeleft, text="Sub Total:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)
        txtSubTotal = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, font=(
            "arial", 13, "bold"), width=29)
        txtSubTotal.grid(row=8, column=1)

        # Total Cost
        lblTotalCost = Label(labelframeleft, text="Total Cost:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)
        txtTotalCost = ttk.Entry(labelframeleft, textvariable=self.var_total, font=(
            "arial", 13, "bold"), width=29)
        txtTotalCost.grid(row=9, column=1)

        # =====Bill Button=====
        btnAdd = Button(labelframeleft, text="Bill", command=self.total, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=10, column=0, padx=1, sticky=W)

        # ======btns======
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # =====Right Side Image=====
        img3 = Image.open(
            r"C:\Users\Vardhan\Desktop\Py Final\Hotel-Management-System\Images\bed.jpg")
        img3 = img3.resize((520, 250), Image.ANTIALIAS)  # Antialias is imp
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbling = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lbling.place(x=760, y=55, width=520, height=250)

        # ======table frame View Details======
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE,
                                 text="View Details", font=("arial", 11, "bold"), padx=2)
        Table_Frame.place(x=435, y=280, width=860, height=490)  # 260

        # lblSearchBy = Label(Table_Frame, font=(
        #     "arial", 11, "bold"), text="Search By:", bg="red", fg="white")
        # lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        # combo_Search = ttk.Combobox(Table_Frame, font=(
        #     "arial", 12, "bold"), width=24, state="readonly")
        # combo_Search["value"] = ("Contact", "Room")
        # combo_Search.current(0)
        # combo_Search.grid(row=0, column=1, padx=2)

        self.var_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.var_search, font=(
            "arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # ======Show data table======
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=0, width=860, height=300)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, column=("Contact", "Check-in", "Check-out", "RoomType",
                                       "RoomAvailable", "Meal", "No.ofDays"), xscrollcommand=scroll_x.set,      yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact", text="Contact")
        self.room_table.heading("Check-in", text="Check-in Date")
        self.room_table.heading("Check-out", text="Check-out Date")
        self.room_table.heading("RoomType", text="Room Type")
        self.room_table.heading("RoomAvailable", text="Room No.")
        self.room_table.heading("Meal", text="Meal")
        self.room_table.heading("No.ofDays", text="No. of Days")

        self.room_table["show"] = "headings"

        self.room_table.column("Contact", width=100)
        self.room_table.column("Check-in", width=100)
        self.room_table.column("Check-out", width=100)
        self.room_table.column("RoomType", width=100)
        self.room_table.column("RoomAvailable", width=100)
        self.room_table.column("Meal", width=100)
        self.room_table.column("No.ofDays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()
    # add data

    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="@Vardhan27", database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_contact.get(),
                        self.var_checkin.get(),
                        self.var_checkout.get(),
                        self.var_roomtype.get(),
                        self.var_roomavailable.get(),
                        self.var_meal.get(),
                        self.var_noofdays.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Room booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Some thing went wrong:{str(es)}", parent=self.root)
    # fetch data

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="@Vardhan27", database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(
                *self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    # getcursor

    def get_cuersor(self, event=""):
        cusrsor_row = self.room_table.focus()
        content = self.room_table.item(cusrsor_row)
        row = content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    # update function
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror(
                "Error", "Please enter Mobile Number", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="@Vardhan27", database="hotel_management")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s", (


                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
                self.var_contact.get()

            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                "Update", "Room details have been updated succesfully", parent=self.root)

   # delete
    def mDelete(self):
        mDelete = messagebox.askyesno(
            "Hotel Management System", "Do you want to delete this", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="@Vardhan27", database="hotel_management")
            my_cursor = conn.cursor()
            query = "delete from room where Contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")

# ============== All Data Fetch================

    def Fetch_contact(self):
        if self.var_contact == "":
            messagebox.showerror(
                "Please enter contact number!", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="@Vardhan27", database="hotel_management")
        my_cursor = conn.cursor()
        query = ("select Name from customer where Mobile=%s")
        value = (self.var_contact.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()

        if row == None:
            messagebox.showerror(
                "Error", "This number is not found", parent=self.root)
        else:
            conn.commit()
            conn.close()

            showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
            showDataframe.place(x=450, y=55, width=300, height=180)

            lblName = Label(showDataframe, text="Name:",
                            font=("arial", 12, "bold"))
            lblName.place(x=0, y=0)

            lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
            lbl.place(x=90, y=0)

            conn = mysql.connector.connect(
                host="localhost", username="root", password="@Vardhan27", database="hotel_management")
        my_cursor = conn.cursor()
        query = ("select Gender from customer where Mobile=%s")
        value = (self.var_contact.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()

        lblGender = Label(showDataframe, text="Gender:",
                          font=("arial", 12, "bold"))
        lblGender.place(x=0, y=30)

        lb2 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
        lb2.place(x=90, y=30)

        conn = mysql.connector.connect(
            host="localhost", username="root", password="@Vardhan27", database="hotel_management")
        my_cursor = conn.cursor()
        query = ("select Email from customer where Mobile=%s")
        value = (self.var_contact.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()

        lblemail = Label(showDataframe, text="Email:",
                         font=("arial", 12, "bold"))
        lblemail.place(x=0, y=60)

        lb3 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
        lb3.place(x=90, y=60)

        conn = mysql.connector.connect(
            host="localhost", username="root", password="@Vardhan27", database="hotel_management")
        my_cursor = conn.cursor()
        query = ("select Nationality from customer where Mobile=%s")
        value = (self.var_contact.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()

        lblNationality = Label(showDataframe, text="Nationality:",
                               font=("arial", 12, "bold"))
        lblNationality.place(x=0, y=90)

        lb4 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
        lb4.place(x=90, y=90)

        conn = mysql.connector.connect(
            host="localhost", username="root", password="@Vardhan27", database="hotel_management")
        my_cursor = conn.cursor()
        query = ("select Address from customer where Mobile=%s")
        value = (self.var_contact.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()

        lbladdress = Label(showDataframe, text="Address:",
                           font=("arial", 12, "bold"))
        lbladdress.place(x=0, y=120)

        lb5 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
        lb5.place(x=90, y=120)

    # search system

    def search(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="@Vardhan27", database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room where " +
                          str(self.search_var.get())+" LIKE '%"+str(self.var_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.romm_table.delete(
                *self.room_table.get_children())
            for i in rows:

                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Luxury"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.1))
            ST = "Rs."+str("%.2f" % ((q5)))
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.1))
            ST = "Rs."+str("%.2f" % ((q5)))
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Double"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.1))
            ST = "Rs."+str("%.2f" % ((q5)))
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.1))
            ST = "Rs."+str("%.2f" % ((q5)))
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Luxury"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.1))
            ST = "Rs."+str("%.2f" % ((q5)))
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Double"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.1))
            ST = "Rs."+str("%.2f" % ((q5)))
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.1))
            ST = "Rs."+str("%.2f" % ((q5)))
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.1))
            ST = "Rs."+str("%.2f" % ((q5)))
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Luxury"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f" % ((q5)*0.1))
            ST = "Rs."+str("%.2f" % ((q5)))
            TT = "Rs."+str("%.2f" % (q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()
