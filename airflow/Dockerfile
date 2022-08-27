FROM apache/airflow:2.1.0 AS airflow

USER root

RUN apt-get update

USER airflow

ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/"
# COPY requirements.txt .
# 
# RUN pip install --user -r requirements.txt
# 
# COPY . .
