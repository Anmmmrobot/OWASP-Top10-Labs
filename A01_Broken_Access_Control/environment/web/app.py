from flask import Flask, request, render_template, redirect, session, jsonify
from db import get_conn

app = Flask(__name__)
app.secret_key = "devkey"


@app.route("/")
def home():
    return redirect("/login")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        conn = get_conn()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE username=%s AND password=%s",(u,p))
            user = cur.fetchone()

        if user:
            session["user_id"] = user["id"]
            session["role"] = user["role"]
            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("dashboard.html")


@app.route("/records")
def records_page():
    return render_template("records.html")

@app.route("/api/records/<int:rid>")
def get_record(rid):

    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM medical_records WHERE id=%s",(rid,))
        record = cur.fetchone()

    # 没有权限验证（Broken Access Control）
    return jsonify(record)


app.run(host="0.0.0.0", port=5000)
