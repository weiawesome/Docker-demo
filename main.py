import os

from flask import Flask, render_template, redirect
from models.Number import Number
from db import db

app = Flask(__name__)

MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "DefaultDb")
MYSQL_USER = os.environ.get("MYSQL_USER", "DefaultUser")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "DefaultPassword")

dns = "mysql+pymysql://{}:{}@{}:3306/{}".format(
    MYSQL_USER, MYSQL_PASSWORD,
    MYSQL_HOST, MYSQL_DATABASE
)

app.config["SQLALCHEMY_DATABASE_URI"] = dns

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    number = db.session.get(Number, 1)
    if number is None:
        new_number = Number(value=0)
        db.session.add(new_number)
        db.session.commit()
        number = new_number
    return render_template("index.html", number=number.value)


@app.route("/add")
def add():
    number = db.session.get(Number, 1)
    number.value = number.value + 1
    db.session.add(number)
    db.session.commit()
    return redirect("/")


@app.route("/subtract")
def subtract():
    number = db.session.get(Number, 1)
    number.value = number.value - 1
    db.session.add(number)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
