# user.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="Get all users")
async def all_users():
    pass

@router.get("/{user_id}", summary="Get user by ID")
async def user_by_id(user_id: int):
    pass

@router.post("/create", summary="Create a new user")
async def create_user():
    pass

@router.put("/update", summary="Update an existing user")
async def update_user():
    pass

@router.delete("/delete", summary="Delete a user")
async def delete_user():
    pass