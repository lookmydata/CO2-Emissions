import pandas as pd

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from default import DEFAULT_ARGS

# Extract Class
from src.etl.extract import Extract

# Transform Classes
from src.etl.transform import Transform
from pipeline.norm_enfermedades import NormEnfermedades

# Load Class
from src.etl.load_delta import Loader


ENTITIES = [ 
    {
        'id': 'desastres_naturales',
        'extract': Extract,
        'transform': Transform,
        'load': Loader
    },
    {
        'id': 'consumo_energia',
        'extract': Extract,
        'transform': Transform,
        'load': Loader
    },
    {
        'id': 'energia_estadistica_mensual',
        'extract': Extract,
        'transform': Transform,
        'load': Loader
    },
    {
        'id': 'energiaco2',
        'extract': Extract,
        'transform': Transform,
        'load': Loader
    },
    {
        'id': 'cancer_male',
        'extract': Extract,
        'transform': NormEnfermedades,
        'load': Loader
    },
    {
        'id': 'cancer_female',
        'extract': Extract,
        'transform': NormEnfermedades,
        'load': Loader
    },
    {
        'id': 'energia_renovable',
        'extract': Extract,
        'transform': Transform,
        'load': Loader
    },
    {
        'id': 'plantas_energia',
        'extract': Extract,
        'transform': Transform,
        'load': Loader
    },
] 


with DAG(
    'ETL',
    default_args=DEFAULT_ARGS,
    description='Main ETL of CO2-Emissions project',
) as dag:


    def extract_to_json(**kwargs):
        return eval(f"{kwargs['extract']}.{kwargs['id']}")()

    
    def transform_xcom(**kwargs):
        ti = kwargs['ti']
        data = ti.xcom_pull(task_ids=f"extract_{kwargs['id']}")
        return eval(f"{kwargs['transform']}.{kwargs['id']}")(data)


    def load_xcom(**kwargs) -> None:
        ti = kwargs['ti']
        data = ti.xcom_pull(task_ids=f"transform_{kwargs['id']}")
        kwargs['load'](data).to_delta(kwargs['id'])


    # Buscar como se traen dos datos (json) con xcom
    def fusion(**kwargs):
        ti = kwargs['ti']
        data = ti.xcom_pull(task_ids=f"extract_cancer_male")
        return eval(f"{kwargs['transform']}.cancer_male")(data)


    for obj in ENTITIES:
        id = obj['id']

        extract = PythonOperator(
            task_id=f'extract_{id}',
            python_callable=extract_to_json,
            op_kwargs=obj,
            provide_context=True,
        )

        transform = PythonOperator(
            task_id=f'transform_{id}',
            python_callable=transform_xcom,
            op_kwargs=obj,
            provide_context=True,
        )

        load = PythonOperator(
            task_id=f'load_{id}',
            python_callable=load_xcom,
            op_kwargs=obj
        )

        if id == 'cancer_male':
            extact_male = extract

        elif id == 'cancer_female':
            extact_female = extract
            transform_female = transform

        else:
            extract >> transform >> load

    else:
        extract[]
