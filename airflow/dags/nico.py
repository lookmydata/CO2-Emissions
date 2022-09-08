import pandas as pd

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from default import DEFAULT_ARGS
from src.etl.transform import T_consumo_energia
from src.etl.transform import T_desastres_naturales
from src.etl.transform import T_energia_estadistica_mensual
from src.etl.transform import T_energyco2
from src.etl.extract_temporal import E_consumo_energia
from src.etl.extract_temporal import E_desastres_naturales
from src.etl.extract_temporal import E_energia_estadistica_mensual
from src.etl.extract_temporal import E_energyco2
from src.etl.load_delta import Loader


ENTITIES = [ 
    {
        'id': 'desastres_naturales',
        'extract': E_desastres_naturales,
        'transform': T_desastres_naturales,
        'load': Loader
    },
    {
        'id': 'consumo_energia',
        'extract': E_consumo_energia,
        'transform': T_consumo_energia,
        'load': Loader
    },
    {
        'id': 'energia_estadistica_mensual',
        'extract': E_energia_estadistica_mensual,
        'transform': T_energia_estadistica_mensual,
        'load': Loader
    },
    {
        'id': 'energyco2',
        'extract': E_energyco2,
        'transform': T_energyco2,
        'load': Loader
    },
] 


with DAG(
    'ETL',
    default_args=DEFAULT_ARGS,
    description='Main ETL of CO2-Emissions project',
    schedule_interval='0 0 20 * *',
) as dag:


    def extract_to_json(**kwargs):
        return kwargs['extract']().to_json()

    
    def transform_xcom(**kwargs):
        ti = kwargs['ti']
        json_df = ti.xcom_pull(task_id=f"extract_{kwargs['id']}")
        return kwargs['transform'](pd.read_json(json_df)).to_json()


    def load_xcom(**kwargs) -> None:
        ti = kwargs['ti']
        json_df = ti.xcom_pull(task_id=f"transform_{kwargs['id']}")
        kwargs['load'](pd.read_json(json_df)).to_delta(kwargs['id'])


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

        extract >> transform >> load
