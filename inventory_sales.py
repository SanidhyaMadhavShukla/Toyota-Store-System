from tkinter import *
from tkinter import ttk,messagebox
from existing import existingClass
from sold import soldClass

class inventoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Toyota Store System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        title=Label(self.root,text="Inventory",font=("goudy old style",40),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000)
        
        self.lbl_existing=Button(self.root,state='disabled',command=self.existing,text="Existing\n Inventory",bg="#33bbf9",fg="white",font=("goudy old style",30,"bold"),bd=5,relief=RIDGE)
        self.lbl_existing.place(x=200,y=120,height=200,width=300)
        
        self.lbl_sold=Button(self.root,command=self.sold,text="Sold\n Inventory",bg="#ff5722",fg="white",font=("goudy old style",30,"bold"),bd=5,relief=RIDGE)
        self.lbl_sold.place(x=600,y=120,height=200,width=300)
    
    def existing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=existingClass(self.new_win)
        
    def sold(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=soldClass(self.new_win)
        
if __name__=="__main__":
    root=Tk()
    obj=inventoryClass(root)
    root.mainloop()