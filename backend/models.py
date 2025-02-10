from sqlalchemy import Column, Integer, String, Date, ForeignKey, func,TIMESTAMP
from sqlalchemy.orm import relationship, Mapped, mapped_column, declarative_base
from sqlalchemy.dialects.postgresql import JSONB, INET, ARRAY
import datetime

Base = declarative_base()

#Таблица с пользователями(хранится логин, хеш пароль, настройки)
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable= False)
    settings: Mapped[dict] = mapped_column(JSONB)

class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

class Devices(Base):
    __tablename__ = 'devices'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable= False) #Внешний ключ пользователей
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey('customers.id'), nullable= False) #Внешний ключ Заказчики
    serial_number: Mapped[str] = mapped_column(String(255), nullable=False)
    production_date: Mapped[datetime.date] = mapped_column(Date)
    execution: Mapped[int] = mapped_column(Integer(10),) #Исполнение(от 1 до 50)
    device_type: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable= False)

    #Зависисмости
    user: Mapped[User] = relationship("User", back_populates="devices")
    customer: Mapped[Customer] = relationship("Customer", back_populates="devices")

    #Связи один к одному
    scanner_details: Mapped[] = relationship("Scaner_details")

class Scaner_details(Base):
    __tablename__ = 'scaner_details'

    pass

class Komrad_details(Base):
    pass

class Rubicon_details(Base):
    pass

class Pik_details(Base):
    pass

class Generator_details(Base):
    pass

