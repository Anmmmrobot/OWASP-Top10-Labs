# A10:2021 - 服务端请求伪造（SSRF）

本项目用于复现 **OWASP Top 10 A10:2021 —— SSRF（Server-Side Request Forgery）漏洞**。  

初始实验环境使用 Docker 部署 DVWA，以实现可复现的漏洞研究环境。  

⚠️ 注意：DVWA 本身 **不包含真实的 SSRF 漏洞模块**，后续的 SSRF 漏洞复现将使用 **OWASP Juice Shop** 完成。

---

## 项目目标

- 理解 SSRF 漏洞原理
- 复现真实漏洞利用场景
- 编写漏洞验证 PoC
- 分析并提出防护与缓解方案

---

## 环境搭建（DVWA）

### 拉取 Docker 镜像

<img src="screenshots/env_01_pull_image.png" width="750">

---

### DVWA 容器运行

<img src="screenshots/env_02_container_running.png" width="750">

---

### DVWA 登录页面

<img src="screenshots/env_03_dvwa_home.png" width="750">

---

### DVWA 数据库初始化

<img src="screenshots/env_04_database_init.png" width="750">

---

### DVWA 登录成功

<img src="screenshots/env_05_login_success.png" width="750">

---

## 环境信息

| 项目 | 内容 |
|---|---|
| 平台 | Docker |
| 目标应用 | DVWA（仅用于环境搭建） |
| 端口 | 8080 |
| 访问地址 | http://localhost:8080 |

---

## SSRF 真实漏洞复现

> ⚠️ DVWA 不包含 SSRF 漏洞模块；后续步骤将使用 **OWASP Juice Shop** 或其他专门的 SSRF 靶场进行漏洞复现。

---

## 项目进度

✅ 环境搭建完成  
⬜ SSRF 漏洞分析（Juice Shop）  
⬜ 漏洞利用与 Payload 测试  
⬜ PoC 编写  
⬜ 漏洞防护分析
