from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def StudentDate():
    return "Student Data"
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/register")
def register():
    return render_template("register.html")
@app.route("/search")
def Search_data():
    return "Search data of student:"
@app.route("/delete")
def deletestudent():
    return "student deleted is"

if __name__=="__main__":
    app.run()
