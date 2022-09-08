import os

class JsonAPI:
    
    def __init__(self, data):
        self.data = data

    def to(self, id):
        path = os.path.join('src/api/v2', f"{id}.json")
        with open(path, 'w') as file:
            file.write(self.data)
