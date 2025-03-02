FROM python:3.10-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de dependências e instale-as
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y netcat-openbsd && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copie o restante do código
COPY . /app/

# Exponha a porta 8000
EXPOSE 8000

# Comando para rodar o servidor (para desenvolvimento)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
