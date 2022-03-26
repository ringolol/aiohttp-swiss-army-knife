FROM python:3.10-alpine

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk --update --upgrade add postgresql-dev python3-dev gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN apk add build-base

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir generated
COPY generated/requirements.txt generated
RUN pip install -r generated/requirements.txt

COPY . .

ENV PYTHONPATH "/code/dramatiq"

RUN apk update
