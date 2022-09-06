from pandas import DataFrame

class JsonAPI:
    
    def __init__(self, data: Dataframe):
        self.data = data

    def to_json(self, name: ):
        self.data.to_json('src/api/v3/')
