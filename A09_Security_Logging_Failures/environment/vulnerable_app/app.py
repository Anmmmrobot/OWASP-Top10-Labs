from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# 模拟数据库
users = {
    "admin": "password123"
}

# HTML 表单模板
login_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Login - OWASP A09</title>
</head>
<body>
    <h2>Login</h2>
    <form method="post" action="/login" id="loginForm">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
"""

@app.route("/login", methods=["GET", "POST"])
def login():
    # GET 请求返回 HTML 表单
    if request.method == "GET":
        return render_template_string(login_form)

    # POST 请求处理登录
    # 支持表单提交和 JSON 提交
    if request.is_json:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
    else:
        username = request.form.get("username")
        password = request.form.get("password")

    # 漏洞特征：没有日志、没有失败记录、没有限速
    if username in users and users[username] == password:
        return jsonify({"msg": "login success"})
    else:
        return jsonify({"msg": "login failed"}), 401

@app.route("/")
def index():
    return "OWASP A09 Vulnerable App"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
