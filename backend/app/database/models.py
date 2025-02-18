from __future__ import annotations
from sqlalchemy import Column, Integer, String, Date, ForeignKey, func,TIMESTAMP, URL, text
from sqlalchemy.orm import relationship, Mapped, mapped_column, declarative_base
from sqlalchemy.dialects.postgresql import JSONB, INET, ARRAY
from typing import List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from config import settings

engine = create_async_engine(settings.DATABASE_URL_asyncpg, echo=True)

# Create a new sessionmaker
async_sess_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_db_session():
    async with async_sess_maker() as session:
        yield session
        
Base = declarative_base()

#Таблица с пользователями(хранится логин, хеш пароль, настройки)
class UserModel(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable= False)
    settings: Mapped[Optional[Dict[str, Any]]] = mapped_column(JSONB)

    #Связь с данными 
    devices: Mapped[List[DeviceModel]] = relationship("Device", back_populates="user")
class CustomerModel(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    devices: Mapped[List[DeviceModel]] = relationship("Device", back_populates="customer")
class DeviceModel(Base):
    __tablename__ = 'devices'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable= False) #Внешний ключ пользователей
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey('customers.id'), nullable= False) #Внешний ключ Заказчики
    serial_number: Mapped[str] = mapped_column(String(255), nullable=False)
    production_date: Mapped[Optional[Date]] = mapped_column(Date)
    execution: Mapped[Optional[int]] = mapped_column(Integer) #Исполнение от 1 до 50
    device_type: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[Date] = mapped_column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at: Mapped[Date] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable= False)

    #Зависисмости
    user: Mapped[UserModel] = relationship("User", back_populates="devices")
    customer: Mapped[CustomerModel] = relationship("Customer", back_populates="devices")

    #Связи один к одному
    scanner_details: Mapped[Optional[Scanner_detailsModel]] = relationship("Scaner_details", back_populates='device', uselist=False)
    comrad_details: Mapped[Optional[Komrad_detailsModel]] = relationship("Komrad_details", back_populates='device', uselist=False)
    rubicon_details: Mapped[Optional[Rubicon_detailsModel]] = relationship("Rubicon_details", back_populates='device', uselist=False)
    pik_details: Mapped[Optional[Pik_detailsModel]] = relationship("Pik_details", back_populates='device', uselist=False)
    generator_details: Mapped[Optional[Generator_detailsModel]] = relationship("Generator_details", back_populates='device', uselist=False)

class Scanner_detailsModel(Base):
    __tablename__ = 'scaner_details'

    device_id: Mapped[int] = mapped_column(Integer, ForeignKey('devices.id', ondelete="CASCADE"), primary_key=True)
    license_start_date: Mapped[Optional[Date]] = mapped_column(Date)
    license_end_date:Mapped[Optional[Date]] = mapped_column(Date)
    ip: Mapped[Optional[str]] = mapped_column(INET)
    additional_ip: Mapped[Optional[str]] = mapped_column(INET)

    #Связь к развязке
    device: Mapped[DeviceModel] = relationship("Device", back_populates="scanner_details")
class Komrad_detailsModel(Base):
    __tablename__ = 'komrad_details'

    device_id: Mapped[int] = mapped_column(Integer, ForeignKey('devices.id', ondelete="CASCADE"), primary_key=True)
    license_start_date: Mapped[Optional[Date]] = mapped_column(Date)
    license_end_date: Mapped[Optional[Date]] = mapped_column(Date)
    tp_type: Mapped[Optional[str]] = mapped_column(String(20))
    license_type: Mapped[Optional[str]] = mapped_column(String(20))
    tp_start_date: Mapped[Optional[Date]] = mapped_column(Date)
    tp_end_date: Mapped[Optional[Date]] = mapped_column(Date)

    #Связь к развязке
    device: Mapped[DeviceModel] = relationship("Device", back_populates="komrad_details")

class Rubicon_detailsModel(Base):
    __tablename__ = 'rubicon_details'

    device_id: Mapped[int] = mapped_column(Integer, ForeignKey('devices.id', ondelete="CASCADE"), primary_key=True)
    start_date: Mapped[Optional[Date]] = mapped_column(Date)
    end_date: Mapped[Optional[Date]] = mapped_column(Date)

    #Связь к развязке
    device: Mapped[DeviceModel] = relationship("Device", back_populates="rubicon_details")

class Pik_detailsModel(Base):
    __tablename__ = 'pik_details'
    
    device_id: Mapped[int] = mapped_column(Integer, ForeignKey('devices.id', ondelete="CASCADE"), primary_key=True)
    license_start_date: Mapped[Optional[Date]] = mapped_column(Date)
    license_end_date: Mapped[Optional[Date]] = mapped_column(Date)

    #Связь к развязке
    device: Mapped[DeviceModel] = relationship("Device", back_populates="pik_details")

class Generator_detailsModel(Base):
    __tablename__ = 'generator_details'

    device_id: Mapped[int] = mapped_column(Integer, ForeignKey('devices.id', ondelete="CASCADE"), primary_key=True)
    license_start_date: Mapped[Optional[Date]] = mapped_column(Date)
    license_end_date: Mapped[Optional[Date]] = mapped_column(Date)
    tp_end_date: Mapped[Optional[Date]] = mapped_column(Date)

    #Связь к развязке
    device: Mapped[DeviceModel] = relationship("Device", back_populates="generator_details")
