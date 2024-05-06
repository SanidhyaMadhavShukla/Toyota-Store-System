from tkinter import *
from tkinter import ttk,messagebox
import sqlite3


class customerClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Toyota Store System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_customer_id=StringVar()
        self.var_customer_name=StringVar()
        self.var_customer_mobile=StringVar()
        self.var_customer_email=StringVar()
        self.var_customer_address=StringVar()
        self.var_customer_dob=StringVar()
        self.var_customer_aadhar=StringVar()
        self.var_customer_pan=StringVar()
        self.var_customer_type=StringVar()
        self.var_customer_gst=StringVar()
        
        #search
        SearchFrame=LabelFrame(self.root,text="Search Customer",relief=RIDGE,bg="white",font=("goudy old style",12,"bold"),bd=2)
        SearchFrame.place(x=250,y=20,width=600,height=70)
        
        #options
        cmd_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","DOB","Name","ID"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmd_search.place(x=10,y=10,width=180)
        cmd_search.current(0)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,command=self.search,cursor="hand2",text="Search",font=("goudy old style",15),bg="#4caf50",fg="white").place(x=410,y=9,width=150,height=30)
        
        #title
        title=Label(self.root,text="Customer Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
        
        #content
        
        #row 1
        lbl_cusid=Label(self.root,text="Cus ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_type=Label(self.root,text="Cus Type",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_mobile=Label(self.root,text="Mobile",font=("goudy old style",15),bg="white").place(x=700,y=150)
        
        txt_cusid=Entry(self.root,textvariable=self.var_customer_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
        cmd_type=ttk.Combobox(self.root,textvariable=self.var_customer_type,values=("Select","Individual","Organization"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmd_type.place(x=500,y=150,width=180)
        cmd_type.current(0)
        txt_mobile=Entry(self.root,textvariable=self.var_customer_mobile,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
        
        #row 2 
        lbl_name=Label(self.root,text="Cus Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=700,y=190)
        
        txt_name=Entry(self.root,textvariable=self.var_customer_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_customer_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_email=Entry(self.root,textvariable=self.var_customer_email,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)
        
        #row 3 
        lbl_gst=Label(self.root,text="G.S.T",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_aadhar=Label(self.root,text="Aadhar",font=("goudy old style",15),bg="white").place(x=350,y=230)
        lbl_pan=Label(self.root,text="PAN",font=("goudy old style",15),bg="white").place(x=700,y=230)
        
        txt_gst=Entry(self.root,textvariable=self.var_customer_gst,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        txt_aadhar=Entry(self.root,textvariable=self.var_customer_aadhar,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
        txt_pan=Entry(self.root,textvariable=self.var_customer_pan,font=("goudy old style",15),bg="lightyellow").place(x=850,y=230,width=180)
        
        #row 4 
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
        
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=180,height=60)
        
        #buttons
        btn_add=Button(self.root,command=self.add,cursor="hand2",text="ADD",font=("goudy old style",15),bg="#2196f3",fg="white").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,command=self.update,cursor="hand2",text="UPDATE",font=("goudy old style",15),bg="#4caf50",fg="white").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,command=self.delete,cursor="hand2",text="DELETE",font=("goudy old style",15),bg="#f44336",fg="white").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,command=self.clear,cursor="hand2",text="CLEAR",font=("goudy old style",15),bg="#607d8b",fg="white").place(x=860,y=305,width=110,height=28)
        
        #EmployeeTable
        cus_frame=Frame(self.root,bd=3,relief=RIDGE)
        cus_frame.place(x=0,y=350,relwidth=1,height=150)
        scroll_y=Scrollbar(cus_frame,orient=VERTICAL)
        scroll_x=Scrollbar(cus_frame,orient=HORIZONTAL)
        
        self.customer_table=ttk.Treeview(cus_frame,columns=("cid","cname","mobile","email","address","dob","aadhar","pan","type","gst"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_y.config(command=self.customer_table.yview)
        scroll_x.config(command=self.customer_table.xview)
        
        self.customer_table.heading("cid",text="Customer ID")
        self.customer_table.heading("cname",text="Name")
        self.customer_table.heading("mobile",text="Mobile")
        self.customer_table.heading("email",text="Email")
        self.customer_table.heading("address",text="Address")
        self.customer_table.heading("dob",text="Date of Birth")
        self.customer_table.heading("aadhar",text="Aadhar")
        self.customer_table.heading("pan",text="P.A.N")
        self.customer_table.heading("type",text="Customer Type")
        self.customer_table.heading("gst",text="G.S.T")
        
        self.customer_table["show"]="headings"
        
        self.customer_table.column("cid",width=100)
        self.customer_table.column("cname",width=100)
        self.customer_table.column("mobile",width=100)
        self.customer_table.column("email",width=100)
        self.customer_table.column("address",width=100)
        self.customer_table.column("dob",width=100)
        self.customer_table.column("aadhar",width=100)
        self.customer_table.column("pan",width=100)
        self.customer_table.column("type",width=100)
        self.customer_table.column("gst",width=100)
        
        self.customer_table.pack(fill=BOTH,expand=1)
        self.customer_table.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
#========================================================================================================    
    def add(self):
        con=sqlite3.connect(database=r'store.db')
        cur = con.cursor()
        try:
            if self.var_customer_id.get()=="":
                messagebox.showerror("Error","Customer ID must be Required",parent=self.root)
            else:
                cur.execute("Select cid from customer where cid=?",(self.var_customer_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Customer ID already exists try another",parent=self.root)
                else:
                    cur.execute("Insert into CUSTOMER(cid,cname,mobile,email,address,dob,aadhar,pan,type,gst) values(?,?,?,?,?,?,?,?,?,?)",
                                (self.var_customer_id.get(),
                                self.var_customer_name.get(),
                                self.var_customer_mobile.get(),
                                self.var_customer_email.get(),
                                self.txt_address.get('1.0',END),
                                self.var_customer_dob.get(),
                                self.var_customer_aadhar.get(),
                                self.var_customer_pan.get(),
                                self.var_customer_type.get(),
                                self.var_customer_gst.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Customer Added Successfully")
                    self.show()
            con.close()
        except Exception as ex:
            con.close()
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#================================================================================
    def show(self):
        con=sqlite3.connect(database=r'store.db')
        cur = con.cursor()
        try:
            cur.execute("select * from customer")
            rows=cur.fetchall()
            self.customer_table.delete(*self.customer_table.get_children())
            for row in rows:
                self.customer_table.insert('', END, values=row)
            con.close()
        except Exception as ex:
            con.close()
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#=======================================================================================
    def get_data(self,ev):
        row=self.customer_table.focus()
        content=(self.customer_table.item(row))
        row=content['values']
        self.var_customer_id.set(row[0])
        self.var_customer_name.set(row[1])
        self.var_customer_mobile.set(row[2])
        self.var_customer_email.set(row[3])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[4])
        self.var_customer_dob.set(row[5])
        self.var_customer_aadhar.set(row[6])
        self.var_customer_pan.set(row[7])
        self.var_customer_type.set(row[8])
        self.var_customer_gst.set(row[9])
#===================================================================================================
    def update(self):
        con=sqlite3.connect(database=r'store.db')
        cur = con.cursor()
        try:
            if self.var_customer_id.get()=="":
                messagebox.showerror("Error","Customer ID must be Required",parent=self.root)
            else:
                cur.execute("Select cid from customer where cid=?",(self.var_customer_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Customer ID is Invalid",parent=self.root)
                else:
                    cur.execute("Update Customer set cname=?,mobile=?,email=?,address=?,dob=?,aadhar=?,pan=?,type=?,gst=? where cid=?",
                                (self.var_customer_name.get(),
                                self.var_customer_mobile.get(),
                                self.var_customer_email.get(),
                                self.txt_address.get('1.0',END),
                                self.var_customer_dob.get(),
                                self.var_customer_aadhar.get(),
                                self.var_customer_pan.get(),
                                self.var_customer_type.get(),
                                self.var_customer_gst.get(),
                                self.var_customer_id.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Customer Updated Successfully")
                    self.show()
            con.close()
        except Exception as ex:
            con.close()
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#=========================================================================================================
    def delete(self):
        con=sqlite3.connect(database=r'store.db')
        cur = con.cursor()
        try:
            if self.var_customer_id.get()=="":
                messagebox.showerror("Error","Customer ID must be Required",parent=self.root)
            else:
                
                cur.execute("Select cid from customer where cid=?",(self.var_customer_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from customer where cid=?",
                                    (self.var_customer_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Customer Removed Successfully")
                        self.clear()
            con.close()
        except Exception as ex:
            con.close()
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#==================================================================================
    def clear(self):
        self.var_customer_name.set("")
        self.var_customer_mobile.set("")
        self.var_customer_email.set("")
        self.txt_address.delete("1.0",END)
        self.var_customer_dob.set("")
        self.var_customer_aadhar.set("")
        self.var_customer_pan.set("")
        self.var_customer_type.set("")
        self.var_customer_gst.set("")
        self.var_customer_id.set("")
        self.var_searchby.set("")
        self.var_searchtxt.set("")
        self.show()
#==========================================================================================
    def search(self):
        con = sqlite3.connect(database=r'store.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "select":
                messagebox.showerror("Error", "Select Search Option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input is required", parent=self.root)
            else:
                search_text = self.var_searchtxt.get()  # Extract the value from StringVar
                if self.var_searchby.get() == "DOB":
                    cur.execute("SELECT * FROM customer WHERE dob=?", (search_text,))
                elif self.var_searchby.get() == "Name":
                    cur.execute("SELECT * FROM customer WHERE name=?", (search_text,))
                else:
                    cur.execute("SELECT * FROM customer WHERE cid=?", (search_text,))
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.customer_table.delete(*self.customer_table.get_children())
                    for row in rows:
                        self.customer_table.insert('', END, values=row)
                    con.close()
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            con.close()
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
            print(ex)
#=============================================================================================
        
if __name__=="__main__":
    root=Tk()
    obj=customerClass(root)
    root.mainloop()