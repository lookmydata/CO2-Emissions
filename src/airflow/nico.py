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
    'extract',
    default_args=DEFAULT_ARGS,
    description='Main ETL of CO2-Emissions project',
    schedule_interval='0 0 20 * *',
) as dag:
    for obj in ENTITIES:
        id = obj['id']
        extract = PythonOperator(
            task_id=f'extract_{id}',
            python_callable=obj['extract'],
            op_kwargs=obj
        )

        transform = PythonOperator(
            task_id=f'transform_{id}',
            python_callable=obj['transform'],
            op_kwargs=obj
        )

        load = PythonOperator(
            task_id=f'load_{id}',
            python_callable=obj['load'],
            op_kwargs=obj
        )

        extract >> transform >> load
