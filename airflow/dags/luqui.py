from airflow import DAG 
from default import DEFAULT_ARGS
from pipeline.norm_enfermedades import norm_enfermedades, getdatamale, getdatafemale
from pipeline.PIPELINE_renewableenergy import gtf_extract, gtf_transform
from pipeline.PIPELINE_powerplant import pp_extract, pp_transform
from pipeline.PIPELINE_climatedisasters import extract_cd, transform_cd


from src.etl.load_delta import Loader

from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

def ejecucion_func():
    norm_enfermedades(getdatamale(),getdatafemale())

def load():
    Loader(ejecucion_func()).to_delta('tabla_enfermedades')

ENTITIES = [ 
    {
        'id': 'enfermedades',
        'extract': [getdatamale,getdatamale],
        'transform': norm_enfermedades,
        'load': Loader
    },
    {
        'id': 'renovables',
        'extract': gtf_extract,
        'transform': gtf_transform,
        'load': Loader
    },
    {
        'id': 'power_plant',
        'extract': pp_extract,
        'transform': pp_transform,
        'load': Loader
    },
    {
        'id': 'climatedisasters',
        'extract': extract_cd,
        'transform': transform_cd,
        'load': Loader
    },
    
] 

with DAG(
    'dag',
    default_args=DEFAULT_ARGS,
    description='dag',
    schedule_interval='0 0 20 * *',
    catchup=False
) as dag:
    for i in ENTITIES:
        Id = i['id']
        if len(i['extract']) == 2:
            ext = PythonOperator(task_id='extraer',python_callable=(i['extract'][0](),i['extract'][1]()), dag=dag)
            trans = PythonOperator(tasks=i['transform'],python_callable=i['transform'](i['extract'][0](),i['extract'][1]()))
            carga = PythonOperator(task_id='load',python_callable=i['load'](i['transform'](i['extract'][0](),i['extract'][1]()).to_delta('load_', i['id'])), dag=dag)
        
        ext = PythonOperator(task_id='extraer',python_callable=i['extract'], dag=dag)
        trans = PythonOperator(task_id='transform',python_callable=i['transform'], dag=dag)
        
        carga = PythonOperator(task_id='load',python_callable=i['load'](i['transform'](i['extract']()).to_delta('load_', i['id'])), dag=dag)
        
        ext >> trans >> carga
        


    

    

    