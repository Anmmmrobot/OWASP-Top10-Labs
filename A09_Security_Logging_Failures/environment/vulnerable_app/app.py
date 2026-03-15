from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟数据库
users = {
    "admin": "password123"
}

@app.route("/login", methods=["POST"])
def login():

    username = request.json.get("username")
    password = request.json.get("password")

    # ❌ 没有日志
    # ❌ 没有失败记录
    # ❌ 没有限速

    if username in users and users[username] == password:
        return jsonify({"msg": "login success"})
    else:
        return jsonify({"msg": "login failed"}), 401


@app.route("/")
def index():
    return "OWASP A09 Vulnerable App"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
