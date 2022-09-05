from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse


API = FastAPI()

API.mount("/static", StaticFiles(directory='static'), name="static")
templates = Jinja2Templates(directory='templates')


@API.get('/api', response_class=HTMLResponse)
async def helloworld(request: Request):
     return templates.TemplateResponse('index.html', {'request': request})
