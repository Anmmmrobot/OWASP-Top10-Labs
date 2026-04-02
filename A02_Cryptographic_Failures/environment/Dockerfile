FROM python:3.9-slim

WORKDIR /app

COPY wheelhouse /wheelhouse
COPY requirements.txt .

RUN pip install --no-cache-dir \
    --no-index \
    --find-links=/wheelhouse \
    -r requirements.txt

COPY app /app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
