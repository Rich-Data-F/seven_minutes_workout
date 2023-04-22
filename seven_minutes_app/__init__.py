from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .models import Workout


db = SQLAlchemy()
app = Flask(__name__)

app.config["SECRET_KEY"] = "secret-key"
# file will be in the same root folder as __init__
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite2"

db.init_app(app)

from . import models

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html", active="index")


@app.route("/enregistrer", methods=["GET", "POST"])
def enregistrer():
    if request.method == "POST":
        workout_done = request.form.get("workout_done")
        comment = request.form.get("comment")
        new_workout = Workout(workout_done=workout_done, comment=comment)
        db.session.add(new_workout)
        db.session.commit()
    return render_template(
        "enregistrer.html", active="enregistrer", date=datetime.utcnow().date()
    )


@app.route("/chaise")
def chaise():
    return render_template(
        "exercice.html",
        n_exer="Premier",
        exercice="Chaise",
        active="chaise",
        image="img_exer/2-wallsit.png",
    )


@app.route("/pompes")
def pompes():
    return render_template(
        "exercice.html",
        n_exer="Deuxième",
        exercice="Pompes",
        active="pompes",
        image="img_exer/3-pushups.png",
    )
