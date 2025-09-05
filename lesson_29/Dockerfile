# Легкий базовий образ
FROM python:3.11-slim

# Встановимо залежності системи (мінімум)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# Робоча директорія в контейнері
WORKDIR /app

ENV PYTHONPATH=/app

# Встановити залежності Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопіювати код застосунку
COPY app.py ./app.py
COPY tests ./tests

# Значення за замовчуванням до підключення БД
ENV DB_HOST=db \
    DB_PORT=5432 \
    DB_NAME=testdb \
    DB_USER=user \
    DB_PASSWORD=pass

# За замовчуванням — просто запустити демонстрацію CRUD
CMD ["python", "app.py"]
