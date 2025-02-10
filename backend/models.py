from sqlalchemy import Column, Integer, String, Date, ForeignKey, func,TIMESTAMP
from sqlalchemy.orm import relationship, Mapped, mapped_column, declarative_base
from sqlalchemy.dialects.postgresql import JSONB, INET, ARRAY
import datetime
from typing import List, Optional, Dict, Any
from __future__ import annotations


Base = declarative_base()

#Таблица с пользователями(хранится логин, хеш пароль, настройки)
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable= False)
    settings: Mapped[Optional[Dict[str, Any]]] = mapped_column(JSONB)

    #Связь с данными 
    devices: Mapped[List[Device]] = relationship("Device", back_populates="user")
class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    devices: Mapped[List[Device]] = relationship("Device", back_populates="customer")
class Device(Base):
    __tablename__ = 'devices'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable= False) #Внешний ключ пользователей
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey('customers.id'), nullable= False) #Внешний ключ Заказчики
    serial_number: Mapped[str] = mapped_column(String(255), nullable=False)
    production_date: Mapped[Optional[Date]] = mapped_column(Date)
    execution: Mapped[int] = mapped_column(Integer(10),) #Исполнение(от 1 до 50)
    device_type: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable= False)

    #Зависисмости
    user: Mapped[User] = relationship("User", back_populates="devices")
    customer: Mapped[Customer] = relationship("Customer", back_populates="devices")

    #Связи один к одному
    scanner_details: Mapped[Optional[Scanner_details]] = relationship("Scaner_details", back_populates='device', uselist=False)
    comrad_details: Mapped[Optional[Komrad_details]] = relationship("Komrad_details", back_populates='device', uselist=False)
    rubicon_details: Mapped[Optional[Rubicon_details]] = relationship("Rubicon_details", back_populates='device', uselist=False)
    pik_details: Mapped[Optional[Pik_details]] = relationship("Pik_details", back_populates='device', uselist=False)
    generator_details: Mapped[Optional[Generator_details]] = relationship("Generator_details", back_populates='device', uselist=False)

class Scanner_details(Base):
    __tablename__ = 'scaner_details'

    device_id: Mapped[int] = mapped_column(Integer, ForeignKey('devices.id', ondelete="CASCADE"), primary_key=True)

class Komrad_details(Base):
    __tablename__ = 'komrad_details'

    pass

class Rubicon_details(Base):
    __tablename__ = 'rubicon_details'

    pass

class Pik_details(Base):
    __tablename__ = 'pik_details'
    
    pass

class Generator_details(Base):
    __tablename__ = 'generator_details'

    pass

