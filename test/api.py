from uvicorn import run
from src.api import API

if __name__ == '__main__':
    run(API, host='127.0.0.1', port=8000)
