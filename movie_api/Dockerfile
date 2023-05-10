FROM python:3.10.6

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /movie_api

COPY ./requirements.txt /movie_api/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /movie_api/

