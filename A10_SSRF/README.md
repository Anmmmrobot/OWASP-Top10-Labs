# A10:2021 - 服务端请求伪造（SSRF）

## 项目简介

本项目复现 OWASP Top 10 中 **A10: Server‑Side Request Forgery (SSRF)** 漏洞，基于 OWASP Juice Shop Docker 环境，从红队攻击视角演示：

* 漏洞识别
* 攻击面分析
* SSRF 利用
* 内网探测
* 逆向线索分析
* 内部接口攻击

目标是构建一条 **真实世界攻击链（Attack Chain）**，而非单点漏洞演示

---

## 实验环境

* OWASP Juice Shop (Docker)
* Burp Suite
* Chrome + Proxy
* Localhost Lab Environment

环境搭建见：

```
environment/docker.md
```

---

## 项目结构

```
A10_SSRF
│
├── environment      # 实验环境搭建
├── vulnerability    # 漏洞原理与攻击面分析
├── exploit          # 利用过程与PoC
└── screenshots      # 实验截图
```

---

## 攻击链概览

```
 攻击者控制输入 URL
        ↓
服务器 Fetch 访问指定的URL
        ↓
  利用 SSRF 原理
        ↓
   内部服务发现
        ↓
  隐藏文件目录 (/ftp)
        ↓
逆向分析线索 (encrypt.pyc)
        ↓
  找到内部隐藏 API 接口
        ↓
权限绕过 (服务器访问url 绕过前端验证)
        ↓
     挑战解决
```

---

## 核心漏洞点

接口：

```
POST /profile/image/url
```

参数：

```
imageUrl
```

服务器直接请求用户提供的 URL，未进行：

* 内网地址过滤
* 协议限制
* 访问控制验证

导致 SSRF

---

## 最终 Exploit Payload

```
imageUrl=http://localhost:3000/solve/challenges/server-side?key=tRy_H4rd3r_n0thIng_iS_Imp0ssibl3
```

效果：

* 服务器以 localhost 身份访问内部接口
* 绕过访问限制
* 成功触发 SSRF Challenge

---

## 技术要点

本实验覆盖真实 SSRF 利用技术：

* Blind SSRF 时序分析
* 内部网络扫描
* 访问控制绕过
* 逆向分析线索
* 内部API滥用

---

## 学习价值

该实验展示了 SSRF 在真实攻击中的典型用途：

| 场景      | 现实攻击 |
| ------- | ---- |
| 内网扫描    | ✔    |
| 调内部 API | ✔    |
| 权限绕过    | ✔    |
| 云环境攻击   | ✔    |

---

## 截图说明

`screenshots/` 包含：

* SSRF 时间差验证
* FTP 内网访问
* Burp Exploit 请求
* Challenge 成功界面

---

## 免责声明

本项目仅用于：

* Web 安全学习
* 漏洞研究
* 防御能力提升

请勿用于非法用途。

---

## 作者

Anmmmrobot
