from flask import Flask,render_template,request

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
    return render_template("register.html")
@app.route("/search")
def Search_data():
    return "Search data of student:"
@app.route("/delete")
def deletestudent():
    return "student deleted is"

if __name__=="__main__":
    app.run()
