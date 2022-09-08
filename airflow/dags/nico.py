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
    {
        'id': 'cancer_male',
        'extract': Extract,
        'transform': Transform,
        'load': Loader,
    },
    {
        'id': 'cancer_female',
        'extract': Extract,
        'transform': Transform,
        'load': Loader,
    },
] 


with DAG(
    'ETL',
    default_args=DEFAULT_ARGS,
    description='Main ETL of CO2-Emissions project',
) as dag:


    def extract_to_json(**kwargs):
        return getattr(kwargs['extract'](), kwargs['id'])()

    
    def transform_xcom(**kwargs):
        ti = kwargs['ti']
        data = ti.xcom_pull(task_ids=f"extract_{kwargs['id']}")
        return getattr(kwargs['transform'](), kwargs['id'])(data)


    def load_xcom(**kwargs) -> None:
        ti = kwargs['ti']
        data = ti.xcom_pull(task_ids=f"transform_{kwargs['id']}")
        kwargs['load'](data).to_delta(kwargs['id'])


    # Buscar como se traen dos datos (json) con xcom
    def merging_cancer(**kwargs):
        ti = kwargs['ti']
        data = ti.xcom_pull(task_ids=["extract_cancer_male", "extract_cancer_male"])
        return Transform().lung_cancer(*data)


    cancer = {
        'id': 'lung_cancer',
        'extract': [],
        'transform': [],
        'load': Loader
    }

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

        if id == 'cancer_male' or id == 'cancer_female':
            cancer['extract'].append(extract)
            cancer['transform'].append(transform)
            load = None

        else:
            extract >> transform >> load


    load_cancer = PythonOperator(
        task_id=f'load_lung_cancer',
        python_callable=load_xcom,
        op_kwargs=cancer
    )

    merge_cancer = PythonOperator(
        task_id=f'merging_lung_cancer',
        python_callable=merging_cancer,
        provide_context=True,
    )

    cancer['extract'][0] >> cancer['transform'][0] >> merge_cancer >> load_cancer
    cancer['extract'][1] >> cancer['transform'][1] >> merge_cancer >> load_cancer
        
