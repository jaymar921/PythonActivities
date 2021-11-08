from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return f"Hello World"
    
@app.route("/admin")
def admin():
    return f"Hello Admin"
    
@app.route("/student/<studentname>")
def student(studentname:str):
    return f"Hello student: {studentname}"
    
@app.route("/user/<name>")
def user(name:str):
    if name == "admin":
        return redirect(url_for("admin"))
    else:
        return redirect(url_for("student"), studentname = name )

if __name__=="__main__":
	app.run(debug=True)