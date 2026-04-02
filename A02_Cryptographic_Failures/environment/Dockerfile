FROM python:3.9-slim

WORKDIR /app

# 拷贝依赖
COPY wheelhouse /wheelhouse
COPY requirements.txt .

# 离线安装
RUN pip install --no-cache-dir \
    --no-index \
    --find-links=/wheelhouse \
    -r requirements.txt

# 拷贝程序
COPY app /app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]