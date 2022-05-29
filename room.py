from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class RoomBooking:
    def __init__(self,root):
        self.root=root 
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")

        #=====variables=====
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        #======Title======
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #======logo======
        img2=Image.open(r"D:\Users\bhavna\Desktop\Python mini proj\Hotel-Management-System\Images\logo.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)  #Antialias is imp
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40) 

        #======labelFrame======
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #======labels and entries======
        #cust Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("arial",13,"bold"),width=20)
        enty_contact.grid(row=0,column=1, sticky=W)

        #Fetch Data Button
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)

        #Check-in-Date
        check_in_date=Label(labelframeleft,text="Check-in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        #Check-out-Date
        check_out_date=Label(labelframeleft,text="Check-out Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)
        txtcheck_out_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        txtcheck_out_date.grid(row=2,column=1)

        #Room Type
        label_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=("Single","Double","Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #Available Room
        lblRoomAvailable=Label(labelframeleft,text="Rooms Available:",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
        txtRoomAvailable.grid(row=4,column=1)

        #Meal
        lblMeal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
        txtMeal.grid(row=5,column=1)

        #No of Days
        lblNoOfDays=Label(labelframeleft,text="No. of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

        #Paid Tax
        lblPaidTax=Label(labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPaidTax.grid(row=7,column=0,sticky=W)
        txtPaidTax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        txtPaidTax.grid(row=7,column=1)

        #Sub Total
        lblSubTotal=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lblSubTotal.grid(row=8,column=0,sticky=W)
        txtSubTotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
        txtSubTotal.grid(row=8,column=1)

        #Total Cost
        lblTotalCost=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblTotalCost.grid(row=9,column=0,sticky=W)
        txtTotalCost=ttk.Entry(labelframeleft,textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        txtTotalCost.grid(row=9,column=1)

        # =====Bill Button=====
        btnAdd=Button(labelframeleft,text="Bill",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=10,column=0,padx=1, sticky=W)

        #======btns======
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        # =====Right Side Image=====
        img3=Image.open(r"D:\Users\bhavna\Desktop\Python mini proj\Hotel-Management-System\Images\bed.jpg")
        img3=img3.resize((520,250),Image.ANTIALIAS)  #Antialias is imp
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbling=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lbling.place(x=760,y=55,width=520,height=250)

        #======table frame search system======
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",11,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,font=("arial",11,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        txtSearch=ttk.Entry(Table_Frame,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #======Show data table======
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("Contact","Check-in","Check-out","RoomType","RoomAvailable","Meal","No.ofDays"),xscrollcommand=scroll_x.set,      yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact",text="Contact")
        self.room_table.heading("Check-in",text="Check-in Date")
        self.room_table.heading("Check-out",text="Check-out Date")
        self.room_table.heading("RoomType",text="Room Type")
        self.room_table.heading("RoomAvailable",text="Room No.")
        self.room_table.heading("Meal",text="Meal")
        self.room_table.heading("No.ofDays",text="No. of Days")

        self.room_table["show"]="headings"

        self.room_table.column("Contact",width=100)
        self.room_table.column("Check-in",width=100)
        self.room_table.column("Check-out",width=100)
        self.room_table.column("RoomType",width=100)
        self.room_table.column("RoomAvailable",width=100)
        self.room_table.column("Meal",width=100)
        self.room_table.column("No.ofDays",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)

    def Fetch_contact(self):
        if self.var_contact == "":
            messagebox.showerror("Please enter contact number!")

if __name__=="__main__":
    root=Tk()
    obj= RoomBooking(root)
    root.mainloop()