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
from src.etl.load_json_api import JsonAPI


ENTITIES = [ 
    {
        'id': 'desastres_naturales',
        'extract': Extract,
        'transform': Transform,
        'load': Loader,
        'api': JsonAPI,
    },
    {
        'id': 'consumo_energia',
        'extract': Extract,
        'transform': Transform,
        'load': Loader,
        'api': JsonAPI,
    },
    {
        'id': 'energia_estadistica_mensual',
        'extract': Extract,
        'transform': Transform,
        'load': Loader,
        'api': JsonAPI,
    },
    {
        'id': 'energiaco2',
        'extract': Extract,
        'transform': Transform,
        'load': Loader,
        'api': JsonAPI,
    },
    {
        'id': 'energia_renovable',
        'extract': Extract,
        'transform': Transform,
        'load': Loader,
        'api': JsonAPI,
    },
    {
        'id': 'plantas_energia',
        'extract': Extract,
        'transform': Transform,
        'load': Loader,
        'api': JsonAPI,
    },
    {
        'id': 'cancer_male',
        'extract': Extract,
        'transform': Transform,
        'load': Loader,
        'api': JsonAPI,
    },
    {
        'id': 'cancer_female',
        'extract': Extract,
        'transform': Transform,
        'load': Loader,
        'api': JsonAPI,
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
        if kwargs['id'] == 'lung_cancer':
            task_ids='merging_lung_cancer'
        else:
            task_ids=f"transform_{kwargs['id']}"
        data = ti.xcom_pull(task_ids=task_ids)
        kwargs['load'](data).to_delta(kwargs['id'])


    def load_api(**kwargs) -> None:
        ti = kwargs['ti']
        if kwargs['id'] == 'lung_cancer':
            task_ids='merging_lung_cancer'
        else:
            task_ids=f"transform_{kwargs['id']}"

        data = ti.xcom_pull(task_ids=task_ids)
        kwargs['load'](data).to_delta(kwargs['id'])


    #  Buscar como se traen dos datos (json) con xcom
    def merging_cancer(**kwargs):
        ti = kwargs['ti']
        data = ti.xcom_pull(task_ids=["transform_cancer_male", "transform_cancer_female"])
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
        
        if id == 'cancer_male' or id == 'cancer_female':
            cancer['extract'].append(extract)
            cancer['transform'].append(transform)

        else:
            load = PythonOperator(
                task_id=f'load_S3_{id}',
                python_callable=load_xcom,
                op_kwargs=obj
            )

            api = PythonOperator(
                task_id=f'load_API_{id}',
                python_callable=load_api,
                op_kwargs=obj
            )
            extract >> transform >> [load, api]
            

    load_cancer = PythonOperator(
        task_id=f'load_S3_lung_cancer',
        python_callable=load_xcom,
        op_kwargs=cancer
    )

    api_cancer = PythonOperator(
        task_id=f'load_API_lung_cancer',
        python_callable=load_api,
        op_kwargs=cancer
    )

    merge_cancer = PythonOperator(
        task_id=f'merging_lung_cancer',
        python_callable=merging_cancer,
        provide_context=True,
    )

    cancer['extract'][0] >> cancer['transform'][0] >> merge_cancer >> [load_cancer, api_cancer]
    cancer['extract'][1] >> cancer['transform'][1] >> merge_cancer >> [load_cancer, api_cancer]
    
        
