# Usar a imagem oficial do Python
FROM python:3.11
LABEL maintainer="raniereWork@outlook.com"

# Defina variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Cria um diretório de trabalho
WORKDIR /code

# Cria um usuário não-root para segurança
RUN adduser --disabled-password --no-create-home duser

# Copia o código e requisitos da aplicação
COPY djangoapp /code/djangoapp
COPY requirements.txt /code/
COPY scripts /scripts

# Instala dependências do sistema e Python
RUN apt-get update && \
    apt-get install -y libpq-dev gcc netcat-openbsd && \
    pip install --upgrade pip && \
    pip install -r /code/requirements.txt && \
    # Cria diretórios e define permissões
    mkdir -p /data/web/static /data/web/media && \
    chown -R duser:duser /data/web && \
    chmod -R 755 /data/web && \
    chmod -R +x /scripts

# Define o diretório de trabalho para a aplicação
WORKDIR /code/djangoapp

# Define o usuário a ser utilizado
USER duser

# Exponha a porta 8000 para a aplicação Django
EXPOSE 8000

# Define o comando padrão para iniciar a aplicação
CMD ["commands.sh"]
