\# A02:2021 - Cryptographic Failures 实验



\## 一、实验目标



本实验用于复现 OWASP Top 10 2021 中的 A02 Cryptographic Failures 漏洞，通过构建存在安全缺陷的 Web 应用，并从攻击者视角完成漏洞利用过程。



实验目标包括：



1\. 理解 JWT 认证机制

2\. 分析弱加密设计带来的安全问题

3\. 学习 Token 伪造攻击流程

4\. 掌握自动化漏洞利用方法



\---



\## 二、实验环境



技术栈如下：



\- Web 框架：Flask

\- 身份认证：JWT

\- 签名算法：HS256

\- 数据库：SQLite

\- 容器环境：Docker

\- 攻击脚本：Python



\---



\## 三、项目目录结构



```

A02\_Cryptographic\_Failures

│

├── environment

│   ├── Dockerfile

│   ├── docker-compose.yml

│   ├── requirements.txt

│   ├── wheelhouse

│   │

│   └── app

│       ├── app.py

│       ├── init\_db.py

│       └── users.db

│

├── exploit

│   ├── exploit.py

│   ├── dump\_users.py

│   └── exploit.sh

│

└── vulnerability

&#x20;   └── README.md

```



\---



\## 四、漏洞原理



该 Web 应用使用 JWT 进行身份认证，但存在严重的加密设计缺陷。



\### 1. 弱 JWT 密钥



应用中使用硬编码密钥：



JWT\_SECRET = "secret123"



问题：



\- 密钥强度过低

\- 易被字典爆破

\- 密钥直接暴露在源码中



\---



\### 2. 信任客户端 Token 数据



管理员权限验证仅依赖 JWT 中的 role 字段：



服务器没有进行数据库校验，而是直接信任客户端提供的数据。



攻击者只需修改 role 为 admin 并重新签名即可获取管理员权限。



\---



\## 五、实验运行步骤



\### Step 1 启动漏洞环境



进入 environment 目录：



```

cd environment

```



启动容器：



```

docker compose up --build

```



浏览器访问：



```

http://localhost:5000

```



出现页面：



OWASP A02 Vulnerable App Running



说明环境启动成功。



\---



\### Step 2 执行攻击



进入 exploit 目录：



```

cd ../exploit

```



运行自动化攻击脚本：



```

python exploit.py

```



\---



\### Step 3 成功结果



终端将输出：



Secret FOUND: secret123  

Admin token generated  

FLAG{OWASP\_A02\_CRYPTOGRAPHIC\_FAILURE}



说明攻击成功。



\---



\## 六、攻击流程



攻击步骤如下：



1\. 登录接口获取普通用户 JWT

2\. 使用字典爆破 JWT Secret

3\. 构造管理员 Payload

4\. 重新签名生成 Token

5\. 访问 /admin 接口

6\. 获取 Flag



\---



\## 七、漏洞影响



攻击者可以：



\- 伪造身份

\- 获取管理员权限

\- 绕过认证机制

\- 访问敏感数据接口



风险等级：Critical



\---



\## 八、OWASP 对应分类



\- A02:2021 Cryptographic Failures

\- A07:2021 Identification and Authentication Failures



\---



\## 九、安全修复建议



1\. 使用高强度随机密钥



示例：



openssl rand -hex 32



2\. 使用环境变量存储密钥



JWT\_SECRET 应从系统环境变量读取。



3\. 服务端进行权限校验



权限信息必须来自数据库，而不是 JWT。



4\. 使用非对称签名算法



推荐使用 RS256。



\---



\## 十、实验总结



使用加密机制并不代表系统安全。



如果密钥强度不足或服务端信任客户端数据，攻击者仍可完全绕过认证。



\*\*安全设计原则：\*\*



永远不要信任客户端提供的权限信息。

