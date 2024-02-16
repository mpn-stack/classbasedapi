FROM python:3.9.7-slim

WORKDIR /app

ADD . /app/

RUN python -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install -r requirements.txt