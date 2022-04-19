FROM python:3.8
# Python not create files pyc 
ENV PYTHONDONTWRITEBYTECODE 1
# Message logger not register in buffer 
ENV PYTHONUNBUFFERED 1
# Defend variable environment version Django Project  
ENV DJANGO_VERSION 3.1.2
# Installing OS Dependencies / update OS Linux container
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
    net-tools \
    inetutils-ping \ 
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*
# Defined work folder (work environment)
WORKDIR /app-bolao
# Copy for workdir of container files of requirements to webapp 
COPY requirements.txt .
# Upgrade pip and setuptools
RUN pip install --no-cache-dir -U pip setuptools && pip install --no-cache-dir -r requirements.txt
# Copy all files for workdir of container 
COPY . .
# Possibly port for access webapp, just for documentation / -P - user this
EXPOSE 8000
# command default load 
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]