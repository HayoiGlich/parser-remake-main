from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional
from datetime import datetime

from backend.app.database.models import UserModel, CustomerModel, DeviceModel

#Create
async def create_user(db: AsyncSession, username: str, password: str, settings: Optional[dict] | None = None) -> UserModel:
    new_user = UserModel(username=username, password=password, settings=settings)
    await db.add(new_user)
    await db.commit()   
    await db.refresh(new_user)
    return new_user

async def create_customer(db: AsyncSession, name: str) -> CustomerModel:
    new_customer = CustomerModel(name=name)
    await db.add(new_customer)
    await db.commit()
    await db.refresh(new_customer)
    return new_customer

async def create_device(db: AsyncSession, serial_number: str, device_type: str):
    new_device = DeviceModel(serial_number=serial_number,
                             device_type=device_type)
    await db.add(new_device)
    await db.commit()
    await db.refresh(new_device)
    return new_device

#Update
async def update_user(db: AsyncSession, user_id: int, username: str, password: str):
    ...
async def update_customer(db: AsyncSession, name: str):

    ...
async def update_device(db: AsyncSession, serial_number: str, device_type: str):
    ...

#Remove
async def remove_user(db: AsyncSession, user_id: int, username: str, password: str):

    ...

async def remove_customer(db: AsyncSession, customer_id: int, name: str):
    ...
async def remove_device(db: AsyncSession, serial_number: str, device_type: str):
    ...

#Read
async def get_user(db: AsyncSession, user_id: int) -> UserModel:
    return await db.get(UserModel, user_id)

async def get_customer(db: AsyncSession, customer_id: int) -> CustomerModel:
    return await db.get(CustomerModel, customer_id)

async def get_device(db: AsyncSession, serial_number: str, device_type: str) -> DeviceModel:
    return await db.get(DeviceModel, serial_number, device_type)
