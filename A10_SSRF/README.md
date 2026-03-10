# A10:2021 - Server-Side Request Forgery (SSRF)

This project reproduces the **OWASP Top 10 A10:2021 SSRF vulnerability** using DVWA in a reproducible Docker environment.

---

## Goals

- Understand SSRF principles
- Reproduce real vulnerability scenarios
- Develop Proof of Concept (PoC)
- Provide mitigation strategies

---

## Environment Setup

### Docker Image Pulled

<img src="screenshots/env_01_pull_image.png" width="750">

---

### DVWA Container Running

<img src="screenshots/env_02_container_running.png" width="750">

---

### DVWA Login Page

<img src="screenshots/env_03_dvwa_home.png" width="750">

---

### DVWA Database Initialization

<img src="screenshots/env_04_database_init.png" width="750">

---

### DVWA Login Success

<img src="screenshots/env_05_login_success.png" width="750">

---

## Environment Information

| Item | Value |
|---|---|
| Platform | Docker |
| Target Application | DVWA |
| Port | 8080 |
| Access URL | http://localhost:8080 |

---

## Project Status

✅ Environment setup completed  
⬜ SSRF vulnerability analysis  
⬜ Exploitation & payload testing  
⬜ PoC development  
⬜ Mitigation analysis
