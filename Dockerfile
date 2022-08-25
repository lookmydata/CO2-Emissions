FROM alpine:3.16.2

ENV PYTHONUNBUFFERED=1
ENV AIRFLOW_HOME=/airflow/home

RUN apk add --update --no-cache python3 \
    && ln -sf ptyhon3 /usr/bin/python \
    && apk add alpine-sdk linux-headers \
               py3-pip python3-dev \
               py3-libxml2 libxml2-dev libxslt-dev \
    && pip3 install --no-cache --upgrade pip setuptools \
    && pip3 install apache-airflow

RUN airflow initdb

CMD ["airflow", "webserver", "-p", "8080"]
