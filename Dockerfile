FROM tiangolo/uwsgi-nginx-flask:python3.8

LABEL maintainer="Jitendra Singh <jitendra.singh.iitg@gmail.com>"

COPY app/requirements.txt /requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

COPY ./app /app
WORKDIR /app
