FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    git ffmpeg curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["bash", "start"]
