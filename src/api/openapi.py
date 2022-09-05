import json

from fastapi.testclient import TestClient
from main import API

client = TestClient(API)
with open('openapi.json', 'w') as file:
    json.dump(client.get('/openapi.json').json(), file, indent=4)
