import pymysql
from flask import Flask, jsonify
import time

app = Flask(__name__)

# 演示用 secret key（不用 Fernet）
SECRET_KEY = b'my_demo_secret_key'

# 数据库连接
def get_db():
    return pymysql.connect(
        host='mysql',
        user='root',
        password='root',
        database='owasp',
        charset='utf8mb4'
    )

# 初始化数据库
def init_db():
    print("[*] Initializing database...")

    conn = None
    for _ in range(30):
        try:
            conn = get_db()
            break
        except pymysql.err.OperationalError:
            print("Waiting for MySQL...")
            time.sleep(2)

    if conn is None:
        raise Exception("Cannot connect to MySQL after waiting!")

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50),
            email VARCHAR(100),
            password VARCHAR(100),
            credit_card VARCHAR(50)
        )
    """)

    cur.execute("DELETE FROM users")

    cur.execute("""
        INSERT INTO users(username,email,password,credit_card)
        VALUES
        ('alice','alice@test.com','alice123','4111111111111111'),
        ('bob','bob@test.com','bob123','5555555555554444'),
        ('admin','admin@test.com','admin123','378282246310005')
    """)

    conn.commit()
    conn.close()
    print("[+] Database ready")

# 漏洞演示接口
@app.route("/api/users")
def get_users():
    conn = get_db()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    init_db()  # 初始化数据库
    app.run(host="0.0.0.0", port=5000, debug=True)