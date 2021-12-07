from flask import Flask,render_template,request,redirect,url_for,session
from database import SAVE_DB,DELETE_STUDENT,GET_ALL,ValidateUser,SAVE_PAYROLL,GET_PAYROLL,DELETE_PAYROLL

app = Flask(__name__)
app.secret_key = "39cm85yu234m98"


@app.route("/employeelist/<message>")
def studentlist(message:str):
    if "username" in session:
        hlist:list=['#','idno','lastname','firstname','position','daily rate','action']
        slist = GET_ALL()
        return render_template("employee_list.html",title="Employee List", studentlist =slist, pageheader = hlist,message = message)
    else:
        return redirect(url_for("index",message="NO PERMISSION"))

@app.route("/")
def studlist():
    return redirect("employeelist/ok")

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
    

@app.route("/<message>")
def index(message:str):
    return render_template("login.html",title="STUDENT LIST",mess=message)


@app.route("/login", methods=["POST"])
def login():
    username:str = request.form["username"]
    password:str = request.form["password"]

    if ValidateUser(username,password):
        session['username'] = username
        return redirect(url_for("studentlist",message="LOGIN ACCEPTED"))
    else:
        return redirect(url_for("index",message="LOGIN FAILED"))

@app.route("/generate_payroll",methods=["POST"])
def generate_payroll():
    DATA:dict = {
        "flag":request.form['flag'],
        "idno":request.form['idno'],
        "name":request.form['name'],
        "rate":request.form['rate'],
        "date_from":request.form['date_from'],
        "date_to":request.form['date_to'],
        "days":request.form['days'],
        "salary":request.form['salary']
    }
    flag:int = SAVE_PAYROLL(DATA)
    if flag == 0:
        return redirect(url_for("studentlist",message="Generated Payroll"))
    return redirect(url_for("studentlist",message="Error Generating Payroll"))

@app.route("/display_payroll")
def display_payroll():
    if "username" in session:
        hlist:list=['#','idno','name','daily rate','date from','date to','number of day(s) worked', 'salary','action']
        slist = GET_PAYROLL()
        return render_template("generate_payroll.html",title="Generated Payroll", studentlist =slist, pageheader = hlist)
    else:
        return redirect(url_for("index",message="NO PERMISSION"))   

@app.route("/delete_payroll",methods=["GET"])
def delete_payroll():
    DELETE_PAYROLL(request.args.get("id"))
    return redirect(url_for("display_payroll"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index",message="LOGOUT SUCCESSFULLY"))

@app.after_request
def after_request(response):
    response.headers.add('Cache-Control', 'no-store,no-cache,must-revalide,post-check=0,pre-check=0')
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)