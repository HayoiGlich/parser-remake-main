from fastapi import APIRouter
from database.models import async_sess_maker, UserModel
from sqlalchemy import select


router = APIRouter(
    prefix = "/users",
    tags=['Получение лицензий']
)

@router.get("")
async def get_users():
    async with async_sess_maker() as session:
        user_id = await UserModel.find_all()
        return {"user_id": user_id}