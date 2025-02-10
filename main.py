from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import uvicorn
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/pages")
oauth2 = OAuth2PasswordBearer(tokenUrl="auth")


@app.get("/auth")
async def auth(request: Request):
    return templates.TemplateResponse(
        "auth.html",
        {"request": request
         })

@app.get("/licenses")
async def licenses(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request
         })

@app.post('/logout')
async def logout(request: Request):
    return templates.TemplateResponse(
        "auth.html",
        {"request": request
         })

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)