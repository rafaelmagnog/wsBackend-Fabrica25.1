
FROM python:3.10-slim

# Variável para saída sem buffer
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de dependências e instala-as
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o restante do código
COPY . /app/

# Expõe a porta 8000
EXPOSE 8000

# Comando para rodar o servidor (para desenvolvimento)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]