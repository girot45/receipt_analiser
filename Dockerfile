FROM python:3.8

# Обновление списка пакетов и установка необходимых пакетов
RUN apt-get update && \
    apt-get install -y libzbar0 ffmpeg libsm6 libxext6 && \
    rm -rf /var/lib/apt/lists/*

# Создание рабочей директории
WORKDIR /receipt_analiser

# Копирование списка зависимостей Python
COPY requirements.txt .

# Установка зависимостей Python
RUN pip install -r requirements.txt

# Копирование остальных файлов проекта
COPY . .

# Запуск приложения
CMD gunicorn server_code:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
