# ===== 基础镜像 =====
FROM python:3.9-slim

# ===== 设置工作目录 =====
WORKDIR /app

# ===== 拷贝离线依赖 =====
COPY requirements_linux /wheels

# ===== 安装 pip 基础工具（离线） =====
RUN pip install --no-index --find-links=/wheels \
    setuptools==68.2.2 \
    wheel==0.41.2 \
    packaging==23.2

# ===== 安装项目依赖（离线） =====
RUN pip install --no-index --find-links=/wheels \
    Flask==2.3.2 \
    PyMySQL==1.1.0 \
    cryptography==41.0.3

# ===== 拷贝应用代码 =====
COPY app/ /app
COPY init_db.sql /app/

# ===== 暴露端口 =====
EXPOSE 5000

# ===== 启动命令 =====
CMD ["python", "app.py"]