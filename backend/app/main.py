from fastapi import FastAPI, Depends, HTTPException, Request
import uvicorn

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)