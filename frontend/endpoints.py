from fastapi import FastAPI, Response, Request
import numpy as np
from PIL import Image
import io
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def mainpage(request: Request):
    return templates.TemplateResponse("mainpage.html", {"request": request})