FROM python:3.7-slim

WORKDIR /app

ADD . /app

RUN apt-get update ##[edited]

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV NAME OpentoAll

CMD ["python","app.py"]
