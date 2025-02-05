import fastapi
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI playground!"}