FROM databricksruntime/standard:9.x

RUN /databricks/python3/bin/pip install pandas datetime airflow
