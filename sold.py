from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class soldClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Toyota Store System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_transaction_id=StringVar()
        self.var_customer_id=StringVar()
        self.var_customer_name=StringVar()
        self.var_model_id=StringVar()
        self.var_model_name=StringVar()
        self.var_release_year=StringVar()
        self.var_model_color=StringVar()
        self.var_number_plate=StringVar()
        self.var_onroad_price=StringVar()
        self.var_employee_id=StringVar()
        self.var_employee_name=StringVar()
        
        #search
        SearchFrame=LabelFrame(self.root,text="Search Sold Cars",relief=RIDGE,bg="white",font=("goudy old style",12,"bold"),bd=2)
        SearchFrame.place(x=250,y=20,width=600,height=70)
        
        #options
        cmd_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Customer ID","Model ID","Transaction ID"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmd_search.place(x=10,y=10,width=180)
        cmd_search.current(0)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,command=self.search,cursor="hand2",text="Search",font=("goudy old style",15),bg="#4caf50",fg="white").place(x=410,y=9,width=150,height=30)
        
        #title
        title=Label(self.root,text="Sold Car Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
        
        #content
        
        #row 1
        lbl_traid=Label(self.root,text="Tra. ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_cusid=Label(self.root,text="Cus. ID",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_cusname=Label(self.root,text="Cus. Name",font=("goudy old style",15),bg="white").place(x=700,y=150)
        
        txt_traid=Entry(self.root,state='readonly',textvariable=self.var_transaction_id,font=("goudy old style",15),bg="lightyellow").place(x=157,y=150,width=180)
        txt_cusid=Entry(self.root,state='readonly',textvariable=self.var_customer_id,font=("goudy old style",15),bg="lightyellow").place(x=500,y=150,width=180)
        txt_cusname=Entry(self.root,state='readonly',textvariable=self.var_customer_name,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
        
        #row 2 
        lbl_modid=Label(self.root,text="Mod. ID",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_modname=Label(self.root,text="Mod. Name",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_yor=Label(self.root,text="Y.O.R",font=("goudy old style",15),bg="white").place(x=700,y=190)
        
        txt_modid=Entry(self.root,state='readonly',textvariable=self.var_model_id,font=("goudy old style",15),bg="lightyellow").place(x=157,y=190,width=180)
        txt_modname=Entry(self.root,state='readonly',textvariable=self.var_model_name,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_yor=Entry(self.root,state='readonly',textvariable=self.var_release_year,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)
        
        #row 3 
        lbl_color=Label(self.root,text="Color",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_numplate=Label(self.root,text="Num. Plate",font=("goudy old style",15),bg="white").place(x=350,y=230)
        lbl_Onroad=Label(self.root,text="Price",font=("goudy old style",15),bg="white").place(x=700,y=230)
        
        txt_color=Entry(self.root,state='readonly',textvariable=self.var_model_color,font=("goudy old style",15),bg="lightyellow").place(x=157,y=230,width=180)
        txt_numplate=Entry(self.root,state='readonly',textvariable=self.var_number_plate,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
        txt_Onroad=Entry(self.root,state='readonly',textvariable=self.var_onroad_price,font=("goudy old style",15),bg="lightyellow").place(x=850,y=230,width=180)
        
        #row 4 
        lbl_empid=Label(self.root,text="Emp. ID",font=("goudy old style",15),bg="white").place(x=50,y=270)
        lbl_empname=Label(self.root,text="Emp. Name",font=("goudy old style",15),bg="white").place(x=350,y=270)
        
        txt_empid=Entry(self.root,state='readonly',textvariable=self.var_employee_id,font=("goudy old style",15),bg="lightyellow").place(x=157,y=270,width=180)
        txt_empname=Entry(self.root,state='readonly',textvariable=self.var_employee_name,font=("goudy old style",15),bg="lightyellow").place(x=500,y=270,width=180)
        
        #buttons
        btn_clear=Button(self.root,command=self.clear,cursor="hand2",text="CLEAR",font=("goudy old style",15),bg="#607d8b",fg="white").place(x=860,y=305,width=110,height=28)
        
        #EmployeeTable
        ein_frame=Frame(self.root,bd=3,relief=RIDGE)
        ein_frame.place(x=0,y=350,relwidth=1,height=150)
        scroll_y=Scrollbar(ein_frame,orient=VERTICAL)
        scroll_x=Scrollbar(ein_frame,orient=HORIZONTAL)
        
        self.existing_table=ttk.Treeview(ein_frame,columns=("tid","cid","cname","mid","mname","roy","color","plate","onroad","eid","ename"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_y.config(command=self.existing_table.yview)
        scroll_x.config(command=self.existing_table.xview)
        
        self.existing_table.heading("tid",text="Transaction ID")
        self.existing_table.heading("cid",text="Customer ID")
        self.existing_table.heading("cname",text="Customer Name")
        self.existing_table.heading("mid",text="Model ID")
        self.existing_table.heading("mname",text="Model Name")
        self.existing_table.heading("roy",text="Release Year")
        self.existing_table.heading("color",text="Color")
        self.existing_table.heading("plate",text="Number Plate")
        self.existing_table.heading("onroad",text="Onroad Price")
        self.existing_table.heading("eid",text="Employee ID")
        self.existing_table.heading("ename",text="Employee Name")
        
        self.existing_table["show"]="headings"
        
        self.existing_table.column("tid",width=100)
        self.existing_table.column("cid",width=100)
        self.existing_table.column("cname",width=100)
        self.existing_table.column("mid",width=100)
        self.existing_table.column("mname",width=100)
        self.existing_table.column("roy",width=100)
        self.existing_table.column("color",width=100)
        self.existing_table.column("plate",width=100)
        self.existing_table.column("onroad",width=100)
        self.existing_table.column("eid",width=100)
        self.existing_table.column("ename",width=100)
        
        self.existing_table.pack(fill=BOTH,expand=1)
        self.existing_table.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
#==================================================================================
    def clear(self):
        self.var_transaction_id.set("")
        self.var_customer_id.set("")
        self.var_customer_name.set("")
        self.var_model_id.set("")
        self.var_model_name.set("")
        self.var_release_year.set("")
        self.var_model_color.set("")
        self.var_number_plate.set("")
        self.var_onroad_price.set("")
        self.var_employee_id.set("")
        self.var_employee_name.set("")
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
                if self.var_searchby.get() == "Customer ID":
                    cur.execute("SELECT * FROM scar WHERE cid=?", (search_text,))
                elif self.var_searchby.get() == "Model ID":
                    cur.execute("SELECT * FROM scar WHERE mid=?", (search_text,))
                else:
                    cur.execute("SELECT * FROM scar WHERE tid=?", (search_text,))
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.existing_table.delete(*self.existing_table.get_children())
                    for row in rows:
                        self.existing_table.insert('', END, values=row)
                    con.close()
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            con.close()
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
            print(ex)
#=============================================================================================
    def get_data(self,ev):
        row=self.existing_table.focus()
        content=(self.existing_table.item(row))
        row=content['values']
        self.var_transaction_id.set(row[0])
        self.var_customer_id.set(row[1])
        self.var_customer_name.set(row[2])
        self.var_model_id.set(row[3])
        self.var_model_name.set(row[4])
        self.var_release_year.set(row[5])
        self.var_model_color.set(row[6])
        self.var_number_plate.set(row[7])
        self.var_onroad_price.set(row[8])
        self.var_employee_id.set(row[9])
        self.var_employee_name.set(row[10])
#===================================================================================================
    def show(self):
        con=sqlite3.connect(database=r'store.db')
        cur = con.cursor()
        try:
            cur.execute("select * from scar")
            rows=cur.fetchall()
            self.existing_table.delete(*self.existing_table.get_children())
            for row in rows:
                self.existing_table.insert('', END, values=row)
            con.close()
        except Exception as ex:
            con.close()
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#=======================================================================================

if __name__=="__main__":
    root=Tk()
    obj=soldClass(root)
    root.mainloop()