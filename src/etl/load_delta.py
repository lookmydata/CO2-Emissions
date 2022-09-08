import os

from deltalake.writer import write_deltalake

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
