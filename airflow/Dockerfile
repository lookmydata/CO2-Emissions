FROM apache/airflow:2.2.3-python3.9 AS airflow

USER root

RUN apt-get update\
    && apt-get install git

USER airflow

ENV PYTHONPATH "/opt/airflow/code:/opt/airflow/code"
COPY requirements.txt .

RUN pip install --user -r requirements.txt

COPY . .
