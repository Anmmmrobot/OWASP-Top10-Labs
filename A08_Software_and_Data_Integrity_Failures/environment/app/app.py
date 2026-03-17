from flask import Flask, request
import pickle
import base64

app = Flask(__name__)

@app.route("/")
def index():
    return "A08 Vulnerable App Running"

# 漏洞点：不安全反序列化
@app.route("/deserialize", methods=["POST"])
def deserialize():
    data = request.form.get("data")

    try:
        decoded = base64.b64decode(data)
        obj = pickle.loads(decoded)   # 漏洞核心,用户可以控制服务器执行任意 Python 对象,本质是远程代码执行 RCE 入口
        return f"Deserialized: {obj}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
