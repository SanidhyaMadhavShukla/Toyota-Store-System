from tkinter import *
from employee import employeeClass
from customer import customerClass
from inventory_sales import inventoryClass
from SearchnBooking import SearchnBookingClass
import os
import time

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Toyota Store System")
        self.root.config(bg="white")
        
        #title
        title=Label(self.root,text="Toyota Store System",font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #logout button
        btn_logout=Button(self.root,command=self.logout,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        
        #clock
        self.lbl_clock=Label(self.root,text="Welcome to Toyota Store System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #Sidebar Menu
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=225,height=565)
        
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20,"bold"),bg="#009688").pack(side=TOP,fill=X)
        
        btn_SearchAndBooking=Button(LeftMenu,text="Search & Booking",command=self.searchnbooking,font=("times new roman",20),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Customer=Button(LeftMenu,text="Customer",command=self.customer,font=("times new roman",20),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_Inventory=Button(LeftMenu,text="Inventory",command=self.inventory,font=("times new roman",20),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        #content
        self.lbl_sales=Label(self.root,text="Total Cars Sold\n[0]",bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"),bd=5,relief=RIDGE)
        self.lbl_sales.place(x=300,y=120,height=200,width=300)
        
        self.lbl_product=Label(self.root,text="Total Cars\n[0]",bg="#ff5722",fg="white",font=("goudy old style",20,"bold"),bd=5,relief=RIDGE)
        self.lbl_product.place(x=650,y=120,height=200,width=300)
        
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",bg="#009688",fg="white",font=("goudy old style",20,"bold"),bd=5,relief=RIDGE)
        self.lbl_employee.place(x=1000,y=120,height=200,width=300)
        
        self.lbl_customer=Label(self.root,text="Total Customers\n[0]",bg="#ffc107",fg="white",font=("goudy old style",20,"bold"),bd=5,relief=RIDGE)
        self.lbl_customer.place(x=300,y=400,height=200,width=300)
        
        #footer
        lbl_footer=Label(self.root,text="Toyota Store System | Developed by Sanidhya Madhav Shukla, Rohan Gupta and Tejwant Singh",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X )
        
        self.update_date_time()
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    
    def customer(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=customerClass(self.new_win)
        
    def inventory(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=inventoryClass(self.new_win)
    
    def searchnbooking(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SearchnBookingClass(self.new_win)
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
        os.remove('variable.txt')
    
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Toyota Store System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()