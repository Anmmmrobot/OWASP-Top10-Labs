# A09:2021 - 安全日志和监控失败（Security logs and monitoring failures）

## 项目简介
  本项目复现 **OWASP Top10 2021 中的 A09 漏洞：安全日志和监控失败**，通过搭建一个简单 Flask Web 应用，演示暴力破解登录过程以及安全事件未记录的情况

## 一、实验环境搭建
### 1. 克隆项目到本地：
```powershell
git clone git@github.com:Anmmmrobot/OWASP-Top10-Labs.git
cd OWASP-Top10-Labs/A09_Security_Logging_Failures/environment
```

### 2. 使用 Docker Desktop 或 CLI 启动环境：
```powershell
docker-compose up -d --build
```
- --build 会根据 Dockerfile 构建镜像
- 容器端口 5000 映射到宿主机 5000，Flask 默认运行在 5000 端口
- 使用 volumes 挂载本地 /vulnerable_app 到容器 /app，修改代码实时生效

### 3. 浏览器访问应用
```powershell
http://localhost:5000
```
页面显示：**OWASP A09 Vulnerable App**

## 二、漏洞说明
- Flask 应用未记录安全事件，如登录失败、异常操作等
- 没有限速或封禁机制
- 默认 Flask 日志只记录 HTTP 请求，不记录用户名、IP、尝试次数等
- 攻击者可以通过暴力破解登录成功，系统无法监控或报警

## 三、漏洞复现过程
### 1.登录界面
访问：
```powershell
http://localhost:5000/login
```
提交同户名密码，返回JSON信息：
- 成功登陆：**{"msg":"login success"}**
- 登录失败：**{"msg":"login failed"}**

### 2.Brute force攻击
在本机终端进入exploit目录（先通过git clone爬取仓库到本地）
```powershell
cd exploit
python brute_force.py
```
攻击输出示例：
- Trying: 123456 -> {'msg': 'login failed'}
- Trying: admin -> {'msg': 'login failed'}
- Trying: password -> {'msg': 'login failed'}
- Trying: 123123 -> {'msg': 'login failed'}
- Trying: password123 -> {'msg': 'login success'}
容器日志示例：
- 172.17.0.1 - - [15/Mar/2026 08:53:40] "POST /login HTTP/1.1" 401 -
- 172.17.0.1 - - [15/Mar/2026 08:53:40] "POST /login HTTP/1.1" 401 -
- 172.17.0.1 - - [15/Mar/2026 08:53:40] "POST /login HTTP/1.1" 200 -

**注意：Flask 日志仅显示 HTTP 状态码，没有记录用户名、IP 或失败次数，这就是 安全日志和监控失败**

### 3.实验截图
- enter_login_interface.png：实验服务器环境搭建
- environment_set_up.png：登录界面环境
- login_success.png：暴力破解成功返回信息
- no_logs.png：容器日志没有安全事件记录

## 四、漏洞原因分析
- 应用缺乏安全日志记录机制
- 登录失败、异常操作没有触发事件
- 没有限速或报警机制
- Flask 默认访问日志无法替代安全监控
