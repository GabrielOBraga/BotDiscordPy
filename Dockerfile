# Use uma imagem base oficial do Python
FROM python:3.11-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

RUN pip3 install --upgrade pip
# Instale as dependências do Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Execute o bot
CMD ["python", "index.py"]