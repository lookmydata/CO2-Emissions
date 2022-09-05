from airflow import DAG
from airflow.operators import python_operator
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
):

