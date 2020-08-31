FROM python:buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /firstwisher

COPY requirements.txt /firstwisher/
COPY . /firstwisher/
WORKDIR /firstwisher

RUN python3 -m pip install -r requirements.txt

