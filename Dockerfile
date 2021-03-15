FROM python:3.7-slim

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt


RUN apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY . /app

EXPOSE 5000

ENV NAME OpentoAll

CMD ["python","app.py"]
