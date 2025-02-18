from fastapi import FastAPI, Depends, HTTPException, Request
import uvicorn
from routers.usersrout import router as user_rout
app = FastAPI()
app.include_router(user_rout)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)