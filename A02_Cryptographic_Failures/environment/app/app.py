from flask import Flask, request, jsonify
import sqlite3
import jwt
import datetime

app = Flask(__name__)

# ==============================
# OWASP A02 漏洞点 1：
# 硬编码弱 JWT 密钥（极易泄露）
# ==============================
JWT_SECRET = "secret123"   # ❌ 弱密钥
JWT_ALG = "HS256"

DB = "users.db"


def get_db():
    return sqlite3.connect(DB)


# ==============================
# 登录接口
# ==============================
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    conn = get_db()
    cur = conn.cursor()

    # ❌ 明文密码存储与比较
    cur.execute(
        "SELECT id, username FROM users WHERE username=? AND password=?",
        (username, password),
    )

    user = cur.fetchone()
    conn.close()

    if not user:
        return jsonify({"msg": "login failed"}), 401

    payload = {
        "id": user[0],
        "username": user[1],
        "role": "user",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)

    return jsonify({"token": token})


# ==============================
# 用户信息接口
# ==============================
@app.route("/profile")
def profile():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"msg": "missing token"}), 401

    try:
        token = token.replace("Bearer ", "")
        data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
    except Exception:
        return jsonify({"msg": "invalid token"}), 403

    return jsonify({
        "user": data["username"],
        "role": data["role"]
    })


# ==============================
# 管理员接口（目标）
# ==============================
@app.route("/admin")
def admin():

    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"msg": "missing token"}), 401

    try:
        token = token.replace("Bearer ", "")
        data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
    except Exception:
        return jsonify({"msg": "invalid token"}), 403

    # ❌ 仅依赖 JWT role 字段
    if data.get("role") != "admin":
        return jsonify({"msg": "forbidden"}), 403

    return jsonify({
        "flag": "FLAG{OWASP_A02_CRYPTOGRAPHIC_FAILURE}"
    })


@app.route("/")
def index():
    return "OWASP A02 Vulnerable App Running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)