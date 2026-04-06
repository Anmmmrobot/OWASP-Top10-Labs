# A01:2021 - 访问控制失效（Broken Access Control）

---

## 一、项目简介

本项目基于 OWASP Top 10 2021 风险榜单第一位漏洞 **A01: Broken Access Control** 进行红队视角复现

项目流程：

* 漏洞产生
* 攻击者侦察
* 权限绕过
* 数据批量窃取
* 渗透证据生成
* 安全修复分析

靶场系统为模拟医疗管理平台 **MedTrack**，包含用户认证、医疗记录管理与 REST API 接口

---

## 二、项目目标

本项目实现以下安全研究目标：

* 构建真实 Web 应用攻击环境
* 复现 IDOR
* 模拟 Red Team 攻击流程
* 编写自动化 Exploit 工具
* 生成渗透测试级漏洞报告
* 展示完整攻击证据链

---

## 三、漏洞说明

**漏洞名称**：Broken Access Control

**OWASP 分类**：A01:2021

**漏洞核心问题**：

服务器未对资源访问执行 Object-Level Authorization 校验，导致已认证用户可以访问其他用户的数据资源

**攻击类型**：

Horizontal Privilege Escalation

**攻击方式**：

修改 API 中的资源 ID 实现越权访问

---

## 四、项目结构

```
A01_Broken_Access_Control
│
├── environment
│   ├── app
│   │   ├── static/...
│   │   ├── templates/...
│   │   ├── auth.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   ├── database.py
│   │   ├── config.py
│   │   └── app.py
│   │
│   ├── requirements/...
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── init_db.py
│
├── exploit
│   ├── exploit.py
│   ├── auth.py
│   ├── idor_attack.py
│   └── privilege_escalation.py
│
├── vulnerability
│   └── A01_Broken_Access_Control.md
│
├── screenshots/...
│
└── README.md
```
---

## 五、环境部署

### 1. 预拉取镜像

docker pull python:3.9-slim

---

### 2. 构建环境

进入 environment 目录：

docker compose build

---

### 3. 启动靶场

docker compose up

访问：

http://localhost:5000

出现 MedTrack Login 页面即部署成功

---

## 六、测试账号

普通用户：

username: alice
password: alice123

---

## 七、漏洞复现流程

### Step 1 — 登录系统

攻击者使用合法账号获取 Session。

---

### Step 2 — API 分析

发现接口：

GET /api/records/<id>

资源 ID 为可预测整数。

---

### Step 3 — 权限绕过

修改 record_id 即可访问他人数据。

服务器未验证资源所有者。

---

### Step 4 — 自动化攻击

执行：

python -m exploit.exploit

Exploit 将：

* 自动登录
* 枚举记录 ID
* 收集敏感医疗数据
* 生成攻击报告

---

## 八、攻击结果

生成目录：

exploit/loot/

包含：

records.json
被窃取的医疗记录数据

report.txt
攻击时间与统计信息

---

## 九、安全影响

可能造成：

* 医疗隐私泄露
* 批量数据外泄
* 合规违规风险
* 企业信誉损害

该漏洞在真实环境中极为常见

---

## 十、修复建议

核心修复原则：

1. 服务端强制 Authorization Check
2. 实施 基于角色的访问控制
3. 使用 UUID 替代递增 ID
4. Default Deny 策略
5. 审计 API 访问日志
