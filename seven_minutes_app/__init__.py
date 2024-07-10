from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

def create_app():
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


    @app.route("/enregistrer")
    def enregistrer():
        return render_template(
            "enregistrer.html", active="enregistrer", date=datetime.now().date() #utcnow().date()
        )


    @app.route("/enregistrer", methods=["POST"])
    def enregistrer_post():
        workout_done = True if request.form.get("done_for_today") == "on" else False
        comment = request.form.get("comment")
        new_workout = models.Workout(workout_done=workout_done, comment=comment)
        db.session.add(new_workout)
        db.session.commit()
        flash(f"Votre entrainement a bien été enregistré !")
        return redirect(url_for("index"))


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

    return app