from flask import Flask, redirect, render_template, request

app = Flask(__name__)

header:list = ["IDNO","LASTNAME","FIRSTNAME","COURSE","LEVEL","ACTION"]

slist:list = [
	{
		"idno":"001",
		"lastname":"abejar",
		"firstname":"jayharron",
		"course":"BSIT",
		"level":"3"
	},
	{
		"idno":"002",
		"lastname":"alpha",
		"firstname":"bravo",
		"course":"BSCS",
		"level":"2"
	}
]

@app.route("/updatestudent", methods=["POST"])
def updatestudent():
	idno:str = request.form['idno']
	lastname:str = request.form['lastname']
	firstame:str = request.form['firstname']
	course:str = request.form['course']
	level:str = request.form['level']

	index:int = -1
	for item in slist:
		if idno==item['idno']:
			index == slist.index(item)

	slist[index]={
				"idno":idno,
				"lastame":lastname,
				"firstname":firstame,
				"course":course,
				"level":level
			}
	return redirect("studentlist")	

@app.route("/deletestudent",methods=['GET'])
def deletestudent():
	idno:str = request.args.get('idno')
	for item in slist:
		if idno==item['idno']:
			slist.remove(item)
	return redirect("studentlist")


@app.route("/savestudent",methods=["POST"])
def savestudent():
	idno:str = request.form['idno']
	lastname:str = request.form['lastname']
	firstame:str = request.form['firstname']
	course:str = request.form['course']
	level:str = request.form['level']

	slist.append(
			{
				"idno":idno,
				"lastame":lastname,
				"firstname":firstame,
				"course":course,
				"level":level
			}
		)
	return redirect("studentlist")

@app.route("/")
def index():
	return "Hello Studentlist"

@app.route("/studentlist", methods=["GET","POST"])
def studentlist():
	return render_template("studentlist.html", list = slist,header=header)

if __name__ == "__main__":
	app.run(debug=True)