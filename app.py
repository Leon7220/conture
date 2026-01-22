from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = "contents.db"


def get_db():
    return sqlite3.connect(DB_NAME)


# 初期化（テーブル作成）
with get_db() as conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS contents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        type TEXT,
        status TEXT,
        rating INTEGER,
        comment TEXT
    )
    """)


@app.route("/")
def index():
    conn = get_db()
    contents = conn.execute("SELECT * FROM contents").fetchall()
    conn.close()
    return render_template("index.html", contents=contents)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        type_ = request.form["type"]
        status = request.form["status"]
        rating = request.form["rating"]
        comment = request.form["comment"]

        conn = get_db()
        conn.execute(
            "INSERT INTO contents (title, type, status, rating, comment) VALUES (?, ?, ?, ?, ?)",
            (title, type_, status, rating, comment)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db()

    if request.method == "POST":
        title = request.form["title"]
        type_ = request.form["type"]
        status = request.form["status"]
        rating = request.form["rating"]
        comment = request.form["comment"]

        conn.execute("""
        UPDATE contents
        SET title=?, type=?, status=?, rating=?, comment=?
        WHERE id=?
        """, (title, type_, status, rating, comment, id))

        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    content = conn.execute(
        "SELECT * FROM contents WHERE id=?", (id,)
    ).fetchone()
    conn.close()

    return render_template("edit.html", content=content)


@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM contents WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
