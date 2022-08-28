FROM apache/airflow:slim-2.3.4-python3.10 AS airflow
 
USER root

RUN apt-get update 

USER airflow

ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/"
# COPY requirements.txt .

# RUN pip install --user -r requirements.txt

COPY . .
