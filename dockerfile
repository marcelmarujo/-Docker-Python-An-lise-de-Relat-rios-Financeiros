# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de dependências
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todos os arquivos do projeto para o contêiner
COPY . .

# Defina o comando padrão para rodar o script de processamento de dados
CMD ["python", "scripts/data_processing.py"]
