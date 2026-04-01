def init_db():
    print("[*] Initializing database...")

    conn = None
    # 等待 mysql 启动（最多 30 次，每 2 秒）
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