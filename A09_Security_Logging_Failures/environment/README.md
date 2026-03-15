# A09 Logging Failure Lab Environment

本文件说明如何在本地搭建 OWASP A09 实验环境，使用 Docker 容器运行 Flask 漏洞应用

---

## 1. 前置条件

- 已安装 [Docker Desktop](https://www.docker.com/products/docker-desktop)（Windows/macOS）
- Windows 用户建议开启 WSL2 backend
- 克隆本仓库到本地

```powershell
git clone https://github.com/Anmmmrobot/OWASP-Top10-Labs.git
cd OWASP-Top10-Labs\A09_Security_Logging_Failures\environment
```

## 2.拉取本地镜像

- 本实验使用 Python 3.10 Alpine 镜像：
```powershell
docker pull python:3.10.20-alpine3.22
```

## 3.启动容器并运行应用

```powershell
docker run -it --name a09_logging_lab -p 5000:5000 -v "D:\A09_clones\OWASP-Top10-Labs\A09_Security_Logging_Failures\environment\vulnerable_app:/app" python:3.10.20-alpine3.22 sh
cd /app
pip install Flask    # 安装依赖（首次运行时需要）
python app.py        # 启动 Flask
```
- 浏览器访问：
```powershell
http://localhost:5000/login
```
