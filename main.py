import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routers.task import router as task_router
from routers.users import router as user_router

app = FastAPI()

@app.get("/", response_class=JSONResponse)
async def welcome():
    return {"message": "Welcome to Taskmanager"}

# Подключение маршрутов
app.include_router(task_router, prefix="/task", tags=["task"])
app.include_router(user_router, prefix="/user", tags=["user"])