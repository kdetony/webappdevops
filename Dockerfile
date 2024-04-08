FROM python:3.10.7-alpine3.16 AS builder
WORKDIR /app
COPY requirements.txt .
COPY app.py .
ADD templates /app/templates
ADD static /app/static
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 8888
CMD python3 app.py
