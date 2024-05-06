from tkinter import *
from tkinter import ttk,messagebox
import sqlite3


class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Toyota Store System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_employee_id=StringVar()
        self.var_employee_name=StringVar()
        self.var_employee_mobile=StringVar()
        self.var_employee_email=StringVar()
        self.var_employee_address=StringVar()
        self.var_employee_dob=StringVar()
        self.var_employee_aadhar=StringVar()
        self.var_employee_pan=StringVar()
        self.var_employee_designation=StringVar()
        self.var_employee_joining=StringVar()
        self.var_employee_salary=StringVar()
        self.var_employee_account=StringVar()
        
        #search
        SearchFrame=LabelFrame(self.root,text="Search Employee",relief=RIDGE,bg="white",font=("goudy old style",12,"bold"),bd=2)
        SearchFrame.place(x=250,y=20,width=600,height=70)
        
        #options
        cmd_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","DOB","Name","ID"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmd_search.place(x=10,y=10,width=180)
        cmd_search.current(0)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,command=self.search,cursor="hand2",text="Search",font=("goudy old style",15),bg="#4caf50",fg="white").place(x=410,y=9,width=150,height=30)
        
        #title
        title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
        
        #content
        
        #row 1
        lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_designation=Label(self.root,text="Designation",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_mobile=Label(self.root,text="Mobile",font=("goudy old style",15),bg="white").place(x=700,y=150)
        
        txt_empid=Entry(self.root,textvariable=self.var_employee_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
        cmd_designation=ttk.Combobox(self.root,textvariable=self.var_employee_designation,values=("Select","Store Manager","Sales Representative"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmd_designation.place(x=500,y=150,width=180)
        cmd_designation.current(0)
        txt_mobile=Entry(self.root,textvariable=self.var_employee_mobile,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
        
        #row 2 
        lbl_name=Label(self.root,text="Emp Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=700,y=190)
        
        txt_name=Entry(self.root,textvariable=self.var_employee_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_employee_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_email=Entry(self.root,textvariable=self.var_employee_email,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)
        
        #row 3 
        lbl_dof=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_aadhar=Label(self.root,text="Aadhar",font=("goudy old style",15),bg="white").place(x=350,y=230)
        lbl_pan=Label(self.root,text="PAN",font=("goudy old style",15),bg="white").place(x=700,y=230)
        
        txt_dof=Entry(self.root,textvariable=self.var_employee_joining,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        txt_aadhar=Entry(self.root,textvariable=self.var_employee_aadhar,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
        txt_pan=Entry(self.root,textvariable=self.var_employee_pan,font=("goudy old style",15),bg="lightyellow").place(x=850,y=230,width=180)
        
        #row 4 
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=350,y=270)
        lbl_account=Label(self.root,text="B/C Account",font=("goudy old style",15),bg="white").place(x=700,y=270)
        
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=180,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_employee_salary,font=("goudy old style",15),bg="lightyellow").place(x=500,y=270,width=180)
        txt_account=Entry(self.root,textvariable=self.var_employee_account,font=("goudy old style",15),bg="lightyellow").place(x=850,y=270,width=180)
        
        #buttons
        btn_add=Button(self.root,command=self.add,cursor="hand2",text="ADD",font=("goudy old style",15),bg="#2196f3",fg="white").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,command=self.update,cursor="hand2",text="UPDATE",font=("goudy old style",15),bg="#4caf50",fg="white").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,command=self.delete,cursor="hand2",text="DELETE",font=("goudy old style",15),bg="#f44336",fg="white").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,command=self.clear,cursor="hand2",text="CLEAR",font=("goudy old style",15),bg="#607d8b",fg="white").place(x=860,y=305,width=110,height=28)
        
        #EmployeeTable
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        scroll_y=Scrollbar(emp_frame,orient=VERTICAL)
        scroll_x=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.employee_table=ttk.Treeview(emp_frame,columns=("eid","ename","mobile","email","address","dob","aadhar","pan","designation","doj","salary","account"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_y.config(command=self.employee_table.yview)
        scroll_x.config(command=self.employee_table.xview)
        
        self.employee_table.heading("eid",text="Employee ID")
        self.employee_table.heading("ename",text="Name")
        self.employee_table.heading("mobile",text="Mobile")
        self.employee_table.heading("email",text="Email")
        self.employee_table.heading("address",text="Address")
        self.employee_table.heading("dob",text="Date of Birth")
        self.employee_table.heading("aadhar",text="Aadhar")
        self.employee_table.heading("pan",text="P.A.N")
        self.employee_table.heading("designation",text="Designation")
        self.employee_table.heading("doj",text="Date of Joining")
        self.employee_table.heading("account",text="Bank Account")
        self.employee_table.heading("salary",text="Salary")
        
        self.employee_table["show"]="headings"
        
        self.employee_table.column("eid",width=100)
        self.employee_table.column("ename",width=100)
        self.employee_table.column("mobile",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("aadhar",width=100)
        self.employee_table.column("pan",width=100)
        self.employee_table.column("designation",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("account",width=100)
        self.employee_table.column("salary",width=100)
        
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
#========================================================================================================    
    def add(self):
        con=sqlite3.connect(database=r'C:\Users\sanid\Desktop\programs for fun\SE Project\store.db')
        cur = con.cursor()
        try:
            if self.var_employee_id.get()=="":
                messagebox.showerror("Error","Employee ID must be Required",parent=self.root)
            else:
                cur.execute("Select eid from employee where eid=?",(self.var_employee_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Employee ID already exists try another",parent=self.root)
                else:
                    cur.execute("Insert into EMPLOYEE(eid,ename,mobile,email,address,dob,aadhar,pan,designation,doj,salary,account) values(?,?,?,?,?,?,?,?,?,?,?,?)",
                                (self.var_employee_id.get(),
                                self.var_employee_name.get(),
                                self.var_employee_mobile.get(),
                                self.var_employee_email.get(),
                                self.txt_address.get('1.0',END),
                                self.var_employee_dob.get(),
                                self.var_employee_aadhar.get(),
                                self.var_employee_pan.get(),
                                self.var_employee_designation.get(),
                                self.var_employee_joining.get(),
                                self.var_employee_salary.get(),
                                self.var_employee_account.get(),))
                    cur.execute("Insert into LOGIN(eid,designation,lid,password) values(?,?,?,?)",
                                (self.var_employee_id.get(),
                                 self.var_employee_designation.get(),
                                 self.var_employee_id.get(),
                                 self.var_employee_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Employee Added Successfully")
                    self.show()
            con.close()
        except Exception as ex:
            con.close()
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#================================================================================
    def show(self):
        con=sqlite3.connect(database=r'C:\Users\sanid\Desktop\programs for fun\SE Project\store.db')
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', END, values=row)
            con.close()
        except Exception as ex:
            con.close()
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#=======================================================================================
    def get_data(self,ev):
        row=self.employee_table.focus()
        content=(self.employee_table.item(row))
        row=content['values']
        self.var_employee_id.set(row[0])
        self.var_employee_name.set(row[1])
        self.var_employee_mobile.set(row[2])
        self.var_employee_email.set(row[3])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[4])
        self.var_employee_dob.set(row[5])
        self.var_employee_aadhar.set(row[6])
        self.var_employee_pan.set(row[7])
        self.var_employee_designation.set(row[8])
        self.var_employee_joining.set(row[9])
        self.var_employee_salary.set(row[10])
        self.var_employee_account.set(row[11])
#===================================================================================================
    def update(self):
        con=sqlite3.connect(database=r'C:\Users\sanid\Desktop\programs for fun\SE Project\store.db')
        cur = con.cursor()
        try:
            if self.var_employee_id.get()=="":
                messagebox.showerror("Error","Employee ID must be Required",parent=self.root)
            else:
                cur.execute("Select eid from employee where eid=?",(self.var_employee_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Employee ID is Invalid",parent=self.root)
                else:
                    cur.execute("Update EMPLOYEE set ename=?,mobile=?,email=?,address=?,dob=?,aadhar=?,pan=?,designation=?,doj=?,salary=?,account=? where eid=?",
                                (self.var_employee_name.get(),
                                self.var_employee_mobile.get(),
                                self.var_employee_email.get(),
                                self.txt_address.get('1.0',END),
                                self.var_employee_dob.get(),
                                self.var_employee_aadhar.get(),
                                self.var_employee_pan.get(),
                                self.var_employee_designation.get(),
                                self.var_employee_joining.get(),
                                self.var_employee_salary.get(),
                                self.var_employee_account.get(),
                                self.var_employee_id.get(),))
                    cur.execute("Update LOGIN set designation=?,user=?,password=? where eid=?",
                                (self.var_employee_designation.get(),
                                 self.var_employee_id.get(),
                                 self.var_employee_name.get(),
                                 self.var_employee_id.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully")
                    self.show()
            con.close()
        except Exception as ex:
            con.close()
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#=========================================================================================================
    def delete(self):
        con=sqlite3.connect(database=r'C:\Users\sanid\Desktop\programs for fun\SE Project\store.db')
        cur = con.cursor()
        try:
            if self.var_employee_id.get()=="":
                messagebox.showerror("Error","Employee ID must be Required",parent=self.root)
            else:
                
                cur.execute("Select eid from employee where eid=?",(self.var_employee_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from EMPLOYEE where eid=?",
                                    (self.var_employee_id.get(),))
                        cur.execute("delete from LOGIN where eid=?",
                                    (self.var_employee_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Employee Removed Successfully")
                        self.clear()
            con.close()
        except Exception as ex:
            con.close()
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#==================================================================================
    def clear(self):
        self.var_employee_name.set("")
        self.var_employee_mobile.set("")
        self.var_employee_email.set("")
        self.txt_address.delete("1.0",END)
        self.var_employee_dob.set("")
        self.var_employee_aadhar.set("")
        self.var_employee_pan.set("")
        self.var_employee_designation.set("")
        self.var_employee_joining.set("")
        self.var_employee_salary.set("")
        self.var_employee_account.set("")
        self.var_employee_id.set("")
        self.var_searchby.set("")
        self.var_searchtxt.set("")
        self.show()
#==========================================================================================
    def search(self):
        con = sqlite3.connect(database=r'C:\Users\sanid\Desktop\programs for fun\SE Project\store.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "select":
                messagebox.showerror("Error", "Select Search Option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input is required", parent=self.root)
            else:
                search_text = self.var_searchtxt.get()  # Extract the value from StringVar
                if self.var_searchby.get() == "DOB":
                    cur.execute("SELECT * FROM employee WHERE dob=?", (search_text,))
                elif self.var_searchby.get() == "Name":
                    cur.execute("SELECT * FROM employee WHERE ename=?", (search_text,))
                else:
                    cur.execute("SELECT * FROM employee WHERE eid=?", (search_text,))
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for row in rows:
                        self.employee_table.insert('', END, values=row)
                    con.close()
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            con.close()
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
            print(ex)
        
if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()