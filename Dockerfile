FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN apt-get update && apt-get install -y netcat-openbsd gcc python3-dev libpq-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]