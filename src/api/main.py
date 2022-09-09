import os
import json

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, JSONResponse
from fastapi.encoders import j


API = FastAPI()

static_path = os.path.join(os.path.dirname(__file__), 'static')
templates_path = os.path.join(os.path.dirname(__file__), 'templates')
json_path = os.path.join(os.path.dirname(__file__), 'v2')

API.mount("/static", StaticFiles(directory=static_path), name="static")
templates = Jinja2Templates(directory=templates_path)


@API.get('/CO2-Emissions/api', response_class=HTMLResponse)
async def api(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@API.get('/CO2-Emissions/hola', response_class=HTMLResponse)
async def helloworld(request: Request):
    return "<h1>HOLA mario<h1>"


@API.get('/CO2-Emissions/api/v2/consumo_energia.json', response_class=HTMLResponse)
async def api(request: Request):
    file = os.path.join(json_path, 'consumo_energia.json')
    return JSONResponse(json.load(file), {'request': request})
