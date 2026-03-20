# 漏洞修复

## 1. 使用非对称加密算法
将 JWT 签名算法从 HS256（对称）改为 RS256（非对称）：
- 服务器用私钥签名
- 客户端或验证端只持有公钥
```python
import jwt

with open("private.pem", "rb") as f:
    private_key = f.read()

payload = {"username": "user", "role": "admin"}
token = jwt.encode(payload, private_key, algorithm="RS256")
```

## 2. 避免硬编码密钥

将密钥保存在环境变量中：
```Bash
export SECRET_KEY="secure_random_key"
```
Flask 中读取：
```python
import os
SECRET_KEY = os.environ.get("SECRET_KEY")
```
## 3. 限制 token 生命周期

exp 字段不要设置过长，建议 15 分钟到 1 小时：
```python
import datetime
payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
```

## 4. 严格校验 token

使用 jwt.decode 时启用验证：
```python
decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
```
捕获异常，防止伪造 token 绕过：
```python
try:
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
except jwt.ExpiredSignatureError:
    return "Token expired", 401
except jwt.InvalidTokenError:
    return "Invalid token", 401
```
