from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/studentlist")
def list():
    header:list =["IDNO","LASTNAME","FIRSTNAME","COURSE","LEVEL"]
    header:list =["IDNO","LASTNAME","FIRSTNAME","COURSE","LEVEL"]
    student_list: list = [
        {
            "idno":"001",
            "lastname":"alpha",
            "firstname":"bravo",
            "course":"BSCPE",
            "level":"4"
        },
        {
            "idno":"002",
            "lastname":"charlie",
            "firstname":"delta",
            "course":"BSIT",
            "level":"3"
        },
        {
            "idno":"003",
            "lastname":"echo",
            "firstname":"foxtrot",
            "course":"BSCS",
            "level":"2"
        }
    ]
    return render_template("studentlist.html",list = student_list, header=header)

if __name__ == "__main__":
    app.run(debug=True)