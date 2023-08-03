# Use an official Python runtime as a parent image
FROM python:3.7-slim

WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]