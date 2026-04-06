FROM python:3.9-slim

WORKDIR /app

COPY requirements ./requirements
COPY requirements.txt .

RUN pip install --no-index \
    --find-links=./requirements \
    -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]