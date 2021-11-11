from flask import Flask,render_template,request,redirect,url_for
from database import SAVE_DB,DELETE_STUDENT,GETALL

app = Flask(__name__)


@app.route("/studentlist")
def studentlist():
    hlist:list=['#','idno','lastname','firstname','course','level','action']
    slist = GETALL()
    return render_template("studentlist.html",title="studentlist", studentlist =slist, pageheader = hlist)

@app.route("/deletestudent",methods=["GET"])
def deletestudent():
    if DELETE_STUDENT(request.args.get("id")):
        return redirect(url_for("studentlist",message="Student Removed"))
    return redirect("studentlist")

@app.route("/addstudent",methods=["POST"])
def addstudent():
    DATA:dict = {
        "flag":request.form['flag'],
        "idno":request.form['idno'],
        "lastname":request.form['lastname'],
        "firstname":request.form['firstname'],
        "course":request.form['course'],
        "level":request.form['level']
    }
    flag:int = SAVE_DB(DATA)
    if flag == 0:
        return redirect(url_for("studentlist",message="Student Added"))
    elif flag == 2:
        return redirect(url_for("studentlist",message="Student Updated"))
    return redirect(url_for("studentlist",message="Error adding student"))
    

@app.route("/")
def index():
    return f"Hello Student web db"


if __name__ == "__main__":
    app.run(debug=True)