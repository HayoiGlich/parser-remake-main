from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    licenses: Mapped["LicenseData"] = relationship("LicenseData", back_populates="owner")
    
class LicenseData(Base):
    __tablename__ = "licenses"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    org_name: Mapped[str] = mapped_column(String, index=True)
    serial_number: Mapped[str] = mapped_column(String, unique=True)
    version: Mapped[int] = mapped_column(Integer, unique=True)
    production_date: Mapped[Date] = mapped_column(Date)
    license_start: Mapped[Date] = mapped_column(Date)
    license_end: Mapped[Date] = mapped_column(Date)
    ip: Mapped[int] = mapped_column(Integer)
    additional_ip: Mapped[int] = mapped_column(Integer)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped["User"] = relationship("User", back_populates="licenses")