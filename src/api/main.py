import os

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse


API = FastAPI()

static_path = os.path.join(os.path.dirname(__file__), 'static')
templates_path = os.path.join(os.path.dirname(__file__), 'templates')

API.mount("/static", StaticFiles(directory=static_path), name="static")
templates = Jinja2Templates(directory=templates_path)


@API.get('/CO2-Emissions/api', response_class=HTMLResponse)
async def helloworld(request: Request):
     return templates.TemplateResponse('index.html', {'request': request})
