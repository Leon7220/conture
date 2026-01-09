from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
dbname = os.getenv("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = \
    f"postgresql+psycopg2://flaskuser:flaskpass@localhost:5432/contents_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    type = db.Column(db.String(20))
    status = db.Column(db.String(20))
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)

@app.route("/")
def index():
    contents = Content.query.all()
    return render_template("index.html", contents=contents)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        content = Content(
            title=request.form["title"],
            type=request.form["type"],
            status=request.form["status"],
            rating=request.form["rating"],
            comment=request.form["comment"]
        )
        db.session.add(content)
        db.session.commit()
        return redirect("/")
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    content = Content.query.get(id)
    if request.method == "POST":
        content.title = request.form["title"]
        content.type = request.form["type"]
        content.status = request.form["status"]
        content.rating = request.form["rating"]
        content.comment = request.form["comment"]
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", content=content)

@app.route("/delete/<int:id>")
def delete(id):
    content = Content.query.get(id)
    db.session.delete(content)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
