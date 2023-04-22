from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", active="index")


@app.route("/chaise")
def chaise():
    return render_template(
        "exercice.html", n_exer="Premier", exercice="Chaise", active="chaise"
    )


@app.route("/pompes")
def pompes():
    return render_template(
        "exercice.html", n_exer="Deuxième", exercice="Pompes", active="pompes"
    )
