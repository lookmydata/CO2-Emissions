import os

from deltalake.writer import write_deltalake
from src.etl.transform import T_desastres_naturales
from src.etl.extract_temporal import E_desastres_naturales

class Loader:

    def __init__(self, data):
        self.data = data

    def to_delta(self, name):
        path = os.path.join('datasets/normalized_delta', name) 
        if not os.path.exists(path):
            os.mkdir(path)

        write_deltalake(
            path, 
            self.data, 
            mode='overwrite', 
            # mode='append' # Descomentar si se quiere hacer un append del producto
        )

extract_data = E_desastres_naturales()
transform_data = T_desastres_naturales(extract_data)

Loader(transform_data).to_delta('hola')
