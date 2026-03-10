# A10:2021 - Server-Side Request Forgery (SSRF)

This project reproduces the **OWASP Top 10 A10:2021 SSRF vulnerability**.  
The initial environment is built using DVWA in Docker for reproducible setup.  
⚠️ Note: DVWA itself does not include a real SSRF module; real SSRF reproduction will use **OWASP Juice Shop** in later steps.

---

## Goals

- Understand SSRF principles
- Reproduce real vulnerability scenarios
- Develop Proof of Concept (PoC)
- Provide mitigation strategies

---

## Environment Setup (DVWA)

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
| Target Application | DVWA (Environment Setup Only) |
| Port | 8080 |
| Access URL | http://localhost:8080 |

---

## SSRF Real Vulnerability Reproduction

> ⚠️ DVWA does not include SSRF; the following steps will use **OWASP Juice Shop** or other dedicated SSRF labs to reproduce the vulnerability.

---

## Project Status

✅ Environment setup completed  
⬜ SSRF vulnerability analysis (Juice Shop)  
⬜ Exploitation & payload testing  
⬜ PoC development  
⬜ Mitigation analysis
