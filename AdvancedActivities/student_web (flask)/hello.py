from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello/<int:score>")
def hello(score:int):
    return render_template("hello.html", mark=score)

if __name__=="__main__":
    app.run(debug=True)