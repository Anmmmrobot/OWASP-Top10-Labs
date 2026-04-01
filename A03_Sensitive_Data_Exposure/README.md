# A03:2021 -- 敏感数据暴露 (Sensitive Data Exposure)

## 1. 项目结构

```
A03_Sensitive_Data_Exposure
│
├─ /environment                # Docker 环境及依赖
│   ├─ Dockerfile
│   ├─ requirements_linux/    # 离线 Python wheel 文件
│   ├─ app/                   # Flask 项目代码
│   │   ├─ app.py
│   │   ├─ config.py
│   │   └─ templates/
│   └─ init_db.sql            # 数据库初始化 SQL
│
├─ /exploit                   # 漏洞复现脚本
│   └─ exploit.py
│
├─ /vulnerability             # 漏洞分析说明
│   └─ A03_analysis.md
│
└─ /screenshots               # 漏洞复现截图及流程图
│
└─ README.md  
```

## 2. 项目说明

本项目演示 OWASP Top 10 A03:2021 Sensitive Data Exposure 漏洞

### 漏洞特征：

- API 未做身份认证或权限控制
- 明文存储敏感信息（密码、信用卡号）
- 返回数据过度暴露，违反最小权限原则

实验环境基于**Docker + Flask + MySQL** 搭建，并提供离线依赖，支持在无网络环境下构建。

## 3. 环境搭建

进入 environment 目录：

```
cd environment
```

构建 Docker 镜像（离线安装依赖）：

```
docker build -t owasp\_a03:demo .
```

启动 MySQL 容器：

```
docker run -d --name a03\_mysql -e MYSQL\_ROOT\_PASSWORD=root -p 3306:3306 mysql:5.7
```

启动 Web 容器：

```
docker run -d --name a03\_web --link a03\_mysql:mysql -p 5000:5000 owasp\_a03:demo
```

检查容器状态：

```
docker ps
```

测试 API：

```
curl http://127.0.0.1:5000/api/users
```

## 4. 漏洞复现



/exploit/exploit.py 提供自动化攻击示例，可抓取所有用户敏感数据，包括密码和信用卡号。



执行示例：



python exploit.py



输出示例：



\[+] Leaked Users:

\- alice | alice123 | 4111111111111111

\- bob   | bob123   | 5555555555554444

\- admin | admin123 | 378282246310005

5\. 漏洞分析



详细分析见 /vulnerability/A03\_analysis.md，包括：



漏洞根本原因

攻击场景

CVSS 风险评估

安全设计建议



主要建议：



强制身份认证 (Authentication)

密码哈希存储 (Hash Passwords)

敏感字段屏蔽 (Mask Sensitive Fields)

数据加密 (Encrypt Sensitive Data)

权限控制 (Access Control)

遵循最小权限原则 (Principle of Least Data Exposure)

6\. 截图说明



/screenshots 包含：



数据抓取演示截图

攻击流程图

数据流示意图

