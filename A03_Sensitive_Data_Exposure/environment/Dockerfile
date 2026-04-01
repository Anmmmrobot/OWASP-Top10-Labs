FROM python:3.9-slim

WORKDIR /app

COPY requirements_linux /wheels

RUN pip install --no-index --find-links=/wheels \
    setuptools==68.2.2 \
    wheel==0.41.2 \
    packaging==23.2

RUN pip install --no-index --find-links=/wheels \
    Flask==2.3.2 \
    PyMySQL==1.1.0 \
    cryptography==41.0.3

COPY app/ /app
COPY init_db.sql /app/

EXPOSE 5000

CMD ["python", "app.py"]
