from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1> Hello, this is the main page </h1>"


@app.route("/chaise")
def chaise():
    return render_template("chaise.html")


@app.route("/pompes")
def pompes():
    return render_template("pompes.html")
