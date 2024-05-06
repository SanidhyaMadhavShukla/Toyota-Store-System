import sqlite3
def create_db():
    con=sqlite3.connect(database=r'store.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS EMPLOYEE(eid TEXT PRIMARY KEY,ename text,mobile text,email text,address text,dob text,aadhar text,pan text,designation text,doj text,salary text,account text)")
    cur.execute("CREATE TABLE IF NOT EXISTS LOGIN(eid TEXT PRIMARY KEY,designation text,lid text,password text)")
    cur.execute("CREATE TABLE IF NOT EXISTS CUSTOMER(cid TEXT PRIMARY KEY,cname text,mobile text,email text,address text,dob text,aadhar text,pan text,type text,gst text)")
    cur.execute("CREATE TABLE IF NOT EXISTS CARS(mid TEXT PRIMARY KEY,fuel text,color text,mname text,roy text,airbags text,range text,mileage text,price text,onroad text,quantity text)")
    cur.execute("CREATE TABLE IF NOT EXISTS SCAR(tid TEXT PRIMARY KEY,cid text,cname text,mid text,mname text,roy text,color text,plate text,onroad text,eid text,ename text)")
    cur.execute("CREATE TABLE IF NOT EXISTS BCAR(cid TEXT PRIMARY KEY,cname text,mid text,mname text,roy text,color text,onroad text,eid text,ename text)")
    con.commit()
    con.close()
create_db()