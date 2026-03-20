FROM python:3.10-slim

WORKDIR /app

COPY environment/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY vulnerability/app /app

EXPOSE 5000

CMD ["python", "app.py"]
