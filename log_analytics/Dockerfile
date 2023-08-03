FROM python:3.7-slim

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y gzip && \
    apt-get install -y geoip-bin && \
    chmod +x /app/*.sh

CMD ["bash", "/app/result.sh"]