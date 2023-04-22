from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1> Hello, this is the main page </h1>"


@app.route("/hello")
def hello_world():
    return "<h1> Hello, World </h1>"
