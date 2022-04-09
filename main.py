from flask import Flask,render_template,request
import sqlite3
#to create connection with db
conn= sqlite3.connect("Studentmanagement.db",check_same_thread=False) #to avoid conflicts use this means storing data in another db instead of this db to avoid such condition
cursor=conn.cursor()
#to check wheter table is present or not
listOfTables=conn.execute("select name from sqlite_master WHERE type='table'AND name='STUDENT'").fetchall()

if listOfTables!=[]:
    print("table already exists")
else:
    conn.execute('''CREATE TABLE STUDENT (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME TEXT, PHONE_NO INTEGER,USERNAME TEXT,EMAIL TEXT,PASSWORD TEXT,CONFIRM_PASSWORD TEXT);''')
    print("Table has created")

app=Flask(__name__)

@app.route("/")
def StudentDate():
    return "Student Data"
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        getName=request.form["name"]
        getPhoneno=request.form["Phoneno"]
        getusername=request.form["username"]
        getemail=request.form["email"]
        getpassword=request.form["password"]
        getconfirmpassword=request.form["cpassword"]
        print(getName)
        print(getPhoneno)
        print(getusername)
        print(getemail)
        print(getpassword)
        print(getconfirmpassword)
        #just inserting values in DB using try ,catch
        try:
            conn.execute("INSERT INTO STUDENT(NAME,PHONE_NO,USERNAME,EMAIL,PASSWORD)VALUES ('"+getName+"','"+getPhoneno+"','"+getusername+"','"+getemail+"','"+getpassword+"')")
            print("Successfully inserted")
        except Exception as e:
            print(e)
    return render_template("register.html")
@app.route("/search")
def Search_data():
    return "Search data of student:"
@app.route("/delete")
def deletestudent():
    return "student deleted is"

if __name__=="__main__":
    app.run()
