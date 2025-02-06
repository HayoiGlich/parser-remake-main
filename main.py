from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import uvicorn
from pathlib import Path

BASE_DIR = Path(__file__).parent
app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "app/frontend/static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / 'app/frontend/pages')

@app.get("/login")
async def auth(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request
         })

@app.get("/licenses")
async def licenses(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request
         })

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)