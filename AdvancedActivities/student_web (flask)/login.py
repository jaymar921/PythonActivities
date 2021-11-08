from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/success")
def success():
    return f"LOGIN ACCEPTED"
    
@app.route("/failed")
def failed():
    return f"LOGIN FAILED"

@app.route("/uservalidation",methods=["POST","GET"])
def uservalidation():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'user':
        return redirect(url_for("success"))
    else:
        return redirect(url_for("failed"))

if __name__ == "__main__":
    app.run(debug = True)