import pandas as pd

# Extract Class
from src.etl.extract import Extract

# Transform Classes
from src.etl.transform import Transform

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


def extract_proccess(**kwargs):
    return getattr(kwargs['extract'](), kwargs['id'])()
    

def transform_proccess(data, **kwargs):
    return getattr(kwargs['transform'](), kwargs['id'])(data)
    

def load_delta(data, **kwargs) -> None:
    kwargs['load'](data).to_delta(kwargs['id'])


def load_api(data, **kwargs) -> None:
    kwargs['load'](data).to_delta(kwargs['id'])


#  Buscar como se traen dos datos (json) con xcom
def merging_cancer(data, **kwargs):
    return Transform().lung_cancer(*data)


cancer = {
    'id': 'lung_cancer',
    'extract': [],
    'transform': [],
    'load': Loader
}


for obj in ENTITIES:
    id = obj['id']

    
    print(f'[*] Procesando {id}...')

    E_json = extract_proccess(**obj)
    T_proccess = transform_proccess(E_json, **obj)

    if id == 'cancer_male':
        T_male = T_proccess
        male_object = obj

    elif id == 'cancer_female':
        T_female = T_proccess
        female_object = obj

    else:
        load_delta(T_proccess, **obj)
        load_api(T_proccess, **obj)


cancer_data = merging_cancer([T_male, T_female])
load_delta(cancer_data, load=Loader, id='lung_cancer')
load_api(cancer_data, load=Loader, id='lung_cancer')
