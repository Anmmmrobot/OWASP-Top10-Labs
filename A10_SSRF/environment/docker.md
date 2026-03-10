# Juice Shop Environment Setup

This document describes how to set up the environment for reproducing SSRF vulnerability using **OWASP Juice Shop** in Docker.

---

## 1. Pull Juice Shop Docker Image

```bash
docker pull bkimminich/juice-shop
```

**Screenshot:** <img src="../screenshots/juice_shop_01_pull_image.png" width="750">

---

## 2. Run Juice Shop Container

```bash
docker run -d --name juice-shop -p 3000:3000 bkimminich/juice-shop
```

**Screenshot:** <img src="../screenshots/juice_shop_02_container_running.png" width="750">

* Ensure port `3000` is not occupied.
* The container should be running in detached mode (`-d`).

---

## 3. Access Juice Shop

Open browser: [http://localhost:3000](http://localhost:3000)

**Screenshot:** <img src="../screenshots/juice_shop_03_home.png" width="750">

* You should see the Juice Shop homepage (orange UI).
* This confirms that the environment is ready for SSRF vulnerability testing.
