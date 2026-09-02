FROM python:3.12-slim

# Define o diretório de trabalho como raiz do projeto
WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia a pasta app para /app
COPY ./app ./app

# O comando uvicorn agora encontra o módulo 'app'
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
