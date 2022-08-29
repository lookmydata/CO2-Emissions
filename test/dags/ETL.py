import yaml
import datetime as dt

from airflow import DAG


with yaml

DEFAULT_ARGS = dict(
    owner="Airflow",
    email_on_failure=False,
    email_on_retry=False,
    email=["h4ckcheek@gmail.com"],
    depends_on_past=False,
)

with DAG(
    dag_id="Main ETL proccess",
    start_date=datetime
)
