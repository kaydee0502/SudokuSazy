FROM python:3.8-slim

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip && pip install -r requirements.txt


RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

#COPY . /app

EXPOSE 5000

ENV NAME OpentoAll

CMD ["python","app.py"]
