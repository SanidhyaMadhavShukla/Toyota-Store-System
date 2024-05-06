from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class existingClass:
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
        
        #search
        SearchFrame=LabelFrame(self.root,text="Search Inventory",relief=RIDGE,bg="white",font=("goudy old style",12,"bold"),bd=2)
        SearchFrame.place(x=250,y=20,width=600,height=70)
        
        #options
        cmd_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Release Year","Name","ID"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmd_search.place(x=10,y=10,width=180)
        cmd_search.current(0)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,command=self.search,cursor="hand2",text="Search",font=("goudy old style",15),bg="#4caf50",fg="white").place(x=410,y=9,width=150,height=30)
        
        #title
        title=Label(self.root,text="Inventory Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
        
        #content
        
        #row 1
        lbl_modid=Label(self.root,text="Model ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_type=Label(self.root,text="Fuel Type",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_color=Label(self.root,text="Model Color",font=("goudy old style",15),bg="white").place(x=700,y=150)
        
        txt_modid=Entry(self.root,textvariable=self.var_model_id,font=("goudy old style",15),bg="lightyellow").place(x=157,y=150,width=180)
        cmd_type=ttk.Combobox(self.root,textvariable=self.var_fuel_type,values=("Select","Diesel","Petrol","Electric","Hydrogen Fuel Cell","Hybrid"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmd_type.place(x=500,y=150,width=180)
        cmd_type.current(0)
        txt_color=Entry(self.root,textvariable=self.var_model_color,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
        
        #row 2 
        lbl_name=Label(self.root,text="Model Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_yor=Label(self.root,text="Y.O.R",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_airbags=Label(self.root,text="Airbags",font=("goudy old style",15),bg="white").place(x=700,y=190)
        
        txt_name=Entry(self.root,textvariable=self.var_model_name,font=("goudy old style",15),bg="lightyellow").place(x=157,y=190,width=180)
        txt_yor=Entry(self.root,textvariable=self.var_release_year,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_airbags=Entry(self.root,textvariable=self.var_airbags,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)
        
        #row 3 
        lbl_range=Label(self.root,text="Range",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_mileage=Label(self.root,text="Mileage",font=("goudy old style",15),bg="white").place(x=350,y=230)
        lbl_price=Label(self.root,text="Price",font=("goudy old style",15),bg="white").place(x=700,y=230)
        
        txt_range=Entry(self.root,textvariable=self.var_range,font=("goudy old style",15),bg="lightyellow").place(x=157,y=230,width=180)
        txt_mileage=Entry(self.root,textvariable=self.var_mileage,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
        txt_price=Entry(self.root,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow").place(x=850,y=230,width=180)
        
        #row 4 
        lbl_onroadprice1=Label(self.root,text="Onroad",font=("goudy old style",15),bg="white").place(x=50,y=270)
        lbl_onroadprice2=Label(self.root,text="Price",font=("goudy old style",15),bg="white").place(x=50,y=300)
        lbl_quantity=Label(self.root,text="Quantity",font=("goudy old style",15),bg="white").place(x=350,y=270)
        
        txt_onroadprice=Entry(self.root,textvariable=self.var_onroad_price,font=("goudy old style",15),bg="lightyellow").place(x=157,y=270,width=180)
        txt_quantity=Entry(self.root,text=self.var_quantity,font=("goudy old style",15),bg="lightyellow").place(x=500,y=270,width=180)
        
        #buttons
        btn_add=Button(self.root,command=self.add,cursor="hand2",text="ADD",font=("goudy old style",15),bg="#2196f3",fg="white").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,command=self.update,cursor="hand2",text="UPDATE",font=("goudy old style",15),bg="#4caf50",fg="white").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,command=self.delete,cursor="hand2",text="DELETE",font=("goudy old style",15),bg="#f44336",fg="white").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,command=self.clear,cursor="hand2",text="CLEAR",font=("goudy old style",15),bg="#607d8b",fg="white").place(x=860,y=305,width=110,height=28)
        
        #EmployeeTable
        ein_frame=Frame(self.root,bd=3,relief=RIDGE)
        ein_frame.place(x=0,y=350,relwidth=1,height=150)
        scroll_y=Scrollbar(ein_frame,orient=VERTICAL)
        scroll_x=Scrollbar(ein_frame,orient=HORIZONTAL)
        
        self.existing_table=ttk.Treeview(ein_frame,columns=("mid","fuel","color","mname","roy","airbags","range","mileage","price","onroad","quantity"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_y.config(command=self.existing_table.yview)
        scroll_x.config(command=self.existing_table.xview)
        
        self.existing_table.heading("mid",text="Model ID")
        self.existing_table.heading("fuel",text="Fuel Type")
        self.existing_table.heading("color",text="Model Color")
        self.existing_table.heading("mname",text="Model Name")
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
        self.existing_table.column("mname",width=100)
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
#========================================================================================================    
    def add(self):
        con=sqlite3.connect(database=r'store.db')
        cur = con.cursor()
    
        if self.var_model_id.get()=="":
            messagebox.showerror("Error","Model ID must be Required",parent=self.root)
        else:
            cur.execute("Select mid from cars where mid=?",(self.var_model_id.get(),))
            row=cur.fetchone()
            if row!=None:
                value=self.var_quantity.get()
                value=int(value)
                value+=1
                value_str=str(value)
                self.var_quantity.set(value)
                cur.execute("Update Cars set quantity=? where mid=?",
                            (self.var_quantity.get(),
                             self.var_model_id.get(),))
                con.commit()
                messagebox.showinfo("Success","Car Added Successfully",parent=self.root)
                self.show()
            else:
                cur.execute("Insert into CARS(mid,fuel,color,mname,roy,airbags,range,mileage,price,onroad,quantity) values(?,?,?,?,?,?,?,?,?,?,?)",
                            (self.var_model_id.get(),
                            self.var_fuel_type.get(),
                            self.var_model_color.get(),
                            self.var_model_name.get(),
                            self.var_release_year.get(),
                            self.var_airbags.get(),
                            self.var_range.get(),
                            self.var_mileage.get(),
                            self.var_price.get(),
                            self.var_onroad_price.get(),
                            "1",))
                con.commit()
                messagebox.showinfo("Success","Car Added Successfully")
                self.show()
        con.close()
        
#================================================================================
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
#===================================================================================================
    def update(self):
        con=sqlite3.connect(database=r'store.db')
        cur = con.cursor()
        try:
            if self.var_model_id.get()=="":
                messagebox.showerror("Error","Cars ID must be Required",parent=self.root)
            else:
                cur.execute("Select mid from cars where mid=?",(self.var_model_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Cars ID is Invalid",parent=self.root)
                else:
                    cur.execute("Update Cars set fuel=?,color=?,mname=?,roy=?,airbags=?,range=?,mileage=?,price=?,onroad=? where mid=?",
                                (self.var_fuel_type.get(),
                                self.var_model_color.get(),
                                self.var_model_name.get(),
                                self.var_release_year.get(),
                                self.var_airbags.get(),
                                self.var_range.get(),
                                self.var_mileage.get(),
                                self.var_price.get(),
                                self.var_onroad_price.get(),
                                self.var_model_id.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Car Updated Successfully")
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
            if self.var_model_id.get()=="":
                messagebox.showerror("Error","Car ID must be Required",parent=self.root)
            else:
                
                cur.execute("Select mid from cars where mid=?",(self.var_model_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("select quantity from cars where mid=?",
                                    (self.var_model_id.get(),))
                        rows=cur.fetchone()
                        value=int(rows[0])
                        value-=1
                        value=str(value)
                        self.var_quantity.set(value)
                        cur.execute("Update cars set quantity=? where mid=?",
                                    (self.var_quantity.get(),
                                     self.var_model_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Car Removed Successfully")
                        self.clear()
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
        
if __name__=="__main__":
    root=Tk()
    obj=existingClass(root)
    root.mainloop()