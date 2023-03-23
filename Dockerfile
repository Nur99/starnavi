FROM python:3.10.6-slim-buster as builder

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    gettext \
    libpq-dev \
    locales  

FROM builder as runner

COPY . /project
WORKDIR /project

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir  && \
    rm -rf ~/.cache/pip && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge   --auto-remove && \
    apt-get clean

COPY runners/django-entrypoint.sh /scripts/
COPY runners/celery-entrypoint.sh /scripts/
COPY runners/celery-beat-entrypoint.sh /scripts/

RUN chmod +x /scripts/django-entrypoint.sh && \
    chmod +x /scripts/celery-entrypoint.sh && \
    chmod +x /scripts/celery-beat-entrypoint.sh
