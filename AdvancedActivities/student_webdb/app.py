from flask import Flask,render_template,request,redirect,url_for
from database import SAVE_DB,DELETE_STUDENT,GETALL

app = Flask(__name__)


@app.route("/studentlist/<message>")
def studentlist(message:str):
    hlist:list=['#','idno','lastname','firstname','course','level','action']
    slist = GETALL()
    return render_template("studentlist.html",title="studentlist", studentlist =slist, pageheader = hlist,message = message)

@app.route("/studentlist")
def studlist():
    return redirect("studentlist/ok")

@app.route("/deletestudent",methods=["GET"])
def deletestudent():
    if DELETE_STUDENT(request.args.get("id")):
        return redirect(url_for("studentlist",message="Student Removed"))
    return redirect("studentlist")

@app.route("/addstudent",methods=["POST"])
def savestudent():
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
    app.run(host="0.0.0.0",debug=True)