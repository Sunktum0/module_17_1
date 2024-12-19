# task.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="Get all tasks")
async def all_tasks():
    pass

@router.get("/{task_id}", summary="Get task by ID")
async def task_by_id(task_id: int):
    pass

@router.post("/create", summary="Create a new task")
async def create_task():
    pass

@router.put("/update", summary="Update an existing task")
async def update_task():
    pass

@router.delete("/delete", summary="Delete a task")
async def delete_task():
    pass