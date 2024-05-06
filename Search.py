from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class searchClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Toyota Store System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_model_id=StringVar()
        self.var_model_name=StringVar()
        self.var_release_year=StringVar()
        self.var_model_color=StringVar()
        self.var_fuel_type=StringVar()
        self.var_airbags=StringVar()
        self.var_range=StringVar()
        self.var_mileage=StringVar()
        self.var_price=StringVar()
        self.var_onroad_price=StringVar()
        self.var_quantity=StringVar()
        self.var_customer_id=StringVar()
        self.var_employee_id=StringVar()
        
        #search
        SearchFrame=LabelFrame(self.root,text="Search Inventory",relief=RIDGE,bg="white",font=("goudy old style",12,"bold"),bd=2)
        SearchFrame.place(x=250,y=20,width=600,height=70)
        
        #options
        cmd_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Model ID","Model Name","Year of Release","Color","Fuel Type","Airbags","Range","Mileage","Price",),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmd_search.place(x=10,y=10,width=180)
        cmd_search.current(0)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,command=self.search,cursor="hand2",text="Search",font=("goudy old style",15),bg="#4caf50",fg="white").place(x=410,y=9,width=150,height=30)
        
        #title
        title=Label(self.root,text="Search Inventory",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
        
        #content
        
        #row 1
        lbl_modid=Label(self.root,text="Model ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_type=Label(self.root,text="Fuel Type",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_color=Label(self.root,text="Model Color",font=("goudy old style",15),bg="white").place(x=700,y=150)
        
        txt_modid=Entry(self.root,state='readonly',textvariable=self.var_model_id,font=("goudy old style",15),bg="lightyellow").place(x=157,y=150,width=180)
        txt_type=Entry(self.root,state='readonly',textvariable=self.var_fuel_type,font=("goudy old style",15),bg="lightyellow").place(x=500,y=150,width=180)
        txt_color=Entry(self.root,state='readonly',textvariable=self.var_model_color,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
        
        #row 2 
        lbl_name=Label(self.root,text="Model Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_yor=Label(self.root,text="Y.O.R",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_airbags=Label(self.root,text="Airbags",font=("goudy old style",15),bg="white").place(x=700,y=190)
        
        txt_name=Entry(self.root,state='readonly',textvariable=self.var_model_name,font=("goudy old style",15),bg="lightyellow").place(x=157,y=190,width=180)
        txt_yor=Entry(self.root,state='readonly',textvariable=self.var_release_year,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_airbags=Entry(self.root,state='readonly',textvariable=self.var_airbags,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)
        
        #row 3 
        lbl_range=Label(self.root,text="Range",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_mileage=Label(self.root,text="Mileage",font=("goudy old style",15),bg="white").place(x=350,y=230)
        lbl_price=Label(self.root,text="Price",font=("goudy old style",15),bg="white").place(x=700,y=230)
        
        txt_range=Entry(self.root,state='readonly',textvariable=self.var_range,font=("goudy old style",15),bg="lightyellow").place(x=157,y=230,width=180)
        txt_mileage=Entry(self.root,state='readonly',textvariable=self.var_mileage,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
        txt_price=Entry(self.root,state='readonly',textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow").place(x=850,y=230,width=180)
        
        #row 4 
        lbl_onroadprice1=Label(self.root,text="Onroad",font=("goudy old style",15),bg="white").place(x=50,y=270)
        lbl_onroadprice2=Label(self.root,text="Price",font=("goudy old style",15),bg="white").place(x=50,y=300)
        lbl_cusid=Label(self.root,text="Cus. ID",font=("goudy old style",15),bg="white").place(x=350,y=270)
        lbl_empid=Label(self.root,text="Emp. ID",font=("goudy old style",15),bg="white").place(x=700,y=270)
        
        txt_onroadprice=Entry(self.root,state='readonly',textvariable=self.var_onroad_price,font=("goudy old style",15),bg="lightyellow").place(x=157,y=270,width=180)
        txt_cusid=Entry(self.root,textvariable=self.var_customer_id,font=("goudy old style",15),bg="lightyellow").place(x=500,y=270,width=180)
        self.var_employee_id.set(str(self.read()))
        txt_empid=Entry(self.root,state='readonly',textvariable=self.var_employee_id,font=("goudy old style",15),bg="lightyellow").place(x=850,y=270,width=180)
        
        #buttons
        btn_book=Button(self.root,command=self.book,cursor="hand2",text="BOOK",font=("goudy old style",15),bg="#f44336",fg="white").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,command=self.clear,cursor="hand2",text="CLEAR",font=("goudy old style",15),bg="#607d8b",fg="white").place(x=860,y=305,width=110,height=28)
        
        #EmployeeTable
        ein_frame=Frame(self.root,bd=3,relief=RIDGE)
        ein_frame.place(x=0,y=350,relwidth=1,height=150)
        scroll_y=Scrollbar(ein_frame,orient=VERTICAL)
        scroll_x=Scrollbar(ein_frame,orient=HORIZONTAL)
        
        self.existing_table=ttk.Treeview(ein_frame,columns=("mid","fuel","color","name","roy","airbags","range","mileage","price","onroad","quantity"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_y.config(command=self.existing_table.yview)
        scroll_x.config(command=self.existing_table.xview)
        
        self.existing_table.heading("mid",text="Model ID")
        self.existing_table.heading("fuel",text="Fuel Type")
        self.existing_table.heading("color",text="Model Color")
        self.existing_table.heading("name",text="Model Name")
        self.existing_table.heading("roy",text="Release Year")
        self.existing_table.heading("airbags",text="Airbags")
        self.existing_table.heading("range",text="Range")
        self.existing_table.heading("mileage",text="Mileage")
        self.existing_table.heading("price",text="Price")
        self.existing_table.heading("onroad",text="Onroad Price")
        self.existing_table.heading("quantity",text="Quantity")
        
        self.existing_table["show"]="headings"
        
        self.existing_table.column("mid",width=100)
        self.existing_table.column("fuel",width=100)
        self.existing_table.column("color",width=100)
        self.existing_table.column("name",width=100)
        self.existing_table.column("roy",width=100)
        self.existing_table.column("airbags",width=100)
        self.existing_table.column("range",width=100)
        self.existing_table.column("mileage",width=100)
        self.existing_table.column("price",width=100)
        self.existing_table.column("onroad",width=100)
        self.existing_table.column("quantity",width=100)
        
        self.existing_table.pack(fill=BOTH,expand=1)
        self.existing_table.bind("<ButtonRelease-1>",self.get_data)
        
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
                if self.var_searchby.get() == "Release Year":
                    cur.execute("SELECT * FROM cars WHERE roy=?", (search_text,))
                elif self.var_searchby.get() == "Name":
                    cur.execute("SELECT * FROM cars WHERE mname=?", (search_text,))
                else:
                    cur.execute("SELECT * FROM cars WHERE mid=?", (search_text,))
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
    def book(self):
        con=sqlite3.connect(database=r'store.db')
        cur = con.cursor()
        try:
            if self.var_model_id.get()=="":
                messagebox.showerror("Error","Model ID must be Required",parent=self.root)
            else:
                cur.execute("select cname from customer where cid=?",(self.var_customer_id.get(),))
                cname=cur.fetchone()
                cname=cname[0]
                cur.execute("select ename from employee where eid=?",(self.var_employee_id.get(),))
                ename=cur.fetchone()
                ename=ename[0]
                cur.execute("Insert into BCAR(cid,cname,mid,mname,roy,color,onroad,eid,ename) values(?,?,?,?,?,?,?,?,?)",
                            (self.var_customer_id.get(),
                             cname,
                             self.var_model_id.get(),
                             self.var_model_name.get(),
                             self.var_release_year.get(),
                             self.var_model_color.get(),
                             self.var_onroad_price.get(),
                             self.var_employee_id.get(),
                             ename,))
                con.commit()
                value=self.var_quantity.get()
                value=int(value)
                value-=1
                value=str(value)
                self.var_quantity.set(value)
                cur.execute("Update CARS set quantity=? where mid=?",
                            (self.var_quantity.get(),
                             self.var_model_id.get(),))
                con.commit()
                self.show()
            con.close()
        except Exception as ex:
            con.close()
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#==================================================================================
    def clear(self):
        self.var_model_id.set("")
        self.var_fuel_type.set("")
        self.var_model_color.set("")
        self.var_model_name.set("")
        self.var_release_year.set("")
        self.var_airbags.set("")
        self.var_range.set("")
        self.var_mileage.set("")
        self.var_price.set("")
        self.var_onroad_price.set("")
        self.var_quantity.set("")
        self.var_searchby.set("")
        self.var_searchtxt.set("")
        self.show()
#==========================================================================================
    def get_data(self,ev):
        row=self.existing_table.focus()
        content=(self.existing_table.item(row))
        row=content['values']
        self.var_model_id.set(row[0])
        self.var_fuel_type.set(row[1])
        self.var_model_color.set(row[2])
        self.var_model_name.set(row[3])
        self.var_release_year.set(row[4])
        self.var_airbags.set(row[5])
        self.var_range.set(row[6])
        self.var_mileage.set(row[7])
        self.var_price.set(row[8])
        self.var_onroad_price.set(row[9])
        self.var_quantity.set(row[10])
        try:
            variable=self.read()
            self.var_employee_id.set(str(variable))
        except Exception as ex:
            con.close()
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
#===================================================================================================
    def show(self):
        con=sqlite3.connect(database=r'store.db')
        cur = con.cursor()
        try:
            cur.execute("select * from cars")
            rows=cur.fetchall()
            self.existing_table.delete(*self.existing_table.get_children())
            for row in rows:
                self.existing_table.insert('', END, values=row)
            con.close()
        except Exception as ex:
            con.close()
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

#=======================================================================================
    def read(self):
        with open('variable.txt','r') as file:
            variable = file.read()
        return variable


if __name__=="__main__":
    root=Tk()
    obj=searchClass(root)
    root.mainloop()