from flask import Flask,render_template,request,redirect
from mysql import connector

app = Flask(__name__)

#Connect to database
database = connector.connect(
    host = "192.168.1.122",
    user = "root",
    password = "",
    database = 'pythontth'
)

@app.route("/studentlist")
def studentlist():
    hlist:list=['#','idno','lastname','firstname','course','level','action']
    sql:str = f"SELECT * FROM `student`"
    cursor = database.cursor(dictionary=True)
    cursor.execute(sql)
    slist:list = cursor.fetchall()
    cursor.close()
    return render_template("studentlist.html",title="studentlist", studentlist =slist, pageheader = hlist)

@app.route("/deletestudent",methods=["GET"])
def deletestudent():
    id:int = request.args.get("id")
    sql:str = f"DELETE FROM `student` WHERE `id`={id}"
    cursor = database.cursor(dictionary=True)
    cursor.execute(sql)
    database.commit()
    cursor.close()
    return redirect("studentlist")

@app.route("/addstudent",methods=["POST"])
def addstudent():
    idno:str = request.form['idno']
    lastname:str = request.form['lastname']
    firstname:str = request.form['firstname']
    course:str = request.form['course']
    level:str = request.form['level']
    sql:str = f"INSERT INTO `student` (`idno`,`lastname`,`firstname`,`course`,`level`) VALUE ('{idno}','{lastname}','{firstname}','{course}','{level}')"
    cursor = database.cursor()
    cursor.execute(sql)
    database.commit()
    cursor.close()
    return redirect("studentlist")
    

@app.route("/")
def index():
    return f"Hello Student web db"


if __name__ == "__main__":
    app.run(debug=True)