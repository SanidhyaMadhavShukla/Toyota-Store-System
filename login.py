from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
import os

class loginClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x500+220+130")
        self.root.title("Toyota Store System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #variable
        self.var_login_ID=StringVar()
        self.var_password=StringVar()
        
        #title
        title=Label(self.root,text="Login",font=("goudy old style",40),bg="#0f4d7d",fg="white").place(width=1000)
        
        #content
        
        #row 1
        lbl_user=Label(self.root,text="Username",font=("goudy old style",30),bg="white").place(x=50,y=100)
        txt_user=Entry(self.root,textvariable=self.var_login_ID,font=("goudy old style",30),bg="lightyellow").place(x=500,y=100,width=400)
        
        #row 2
        lbl_pass=Label(self.root,text="Password",font=("goudy old style",30),bg="white").place(x=50,y=200)
        txt_pass=Entry(self.root,textvariable=self.var_password,font=("goudy old style",30),bg="lightyellow").place(x=500,y=200,width=400)
        
        #button
        btn_login=Button(self.root,command=self.login,cursor="hand2",text="LOGIN",font=("goudy old style",30),bg="#607d8b",fg="white").place(x=400,y=300,width=200)

    def login(self):
        con=sqlite3.connect(database=r'store.db')
        cur = con.cursor()
        try:
            if self.var_login_ID.get()=="":
                messagebox.showerror("Error","Login ID must be Required",parent=self.root)
            elif self.var_login_ID.get()=="":
                messagebox.showerror("Error","Password must be Required",parent=self.root)
            else:
                cur.execute("Select designation,eid from login where lid=? AND password=?",(self.var_login_ID.get(),self.var_password.get(),))
                row=cur.fetchone()
                if row!=None:
                    if row[0]=="Store Manager":
                        self.write(row[1])
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python dashboard_sales.py")
                else:
                    messagebox.showerror("Error","Invalid Username or password",parent=self.root)
            con.commit()
            con.close()
        except Exception as ex:
            con.close()
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
    
    def write(self,variable):
        with open('variable.txt','w') as file:
            file.write(str(variable))

if __name__=="__main__":
    root=Tk()
    obj=loginClass(root)
    root.mainloop()