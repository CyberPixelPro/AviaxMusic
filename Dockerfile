FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip nodejs npm ffmpeg

COPY . /app/
WORKDIR /app/

RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD bash start
