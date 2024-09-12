from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, TIMESTAMP, Numeric
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from datetime import datetime, timezone
from .database import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, index=True)
    admin_id = Column(Integer, ForeignKey("admins.id"))

    employees = relationship("Employee", back_populates="company")
    # clients = relationship("Client", back_populates="company")
    admin = relationship("Admin", back_populates="company")


class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String, unique=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="employees")


# class Client(Base):
#     __tablename__ = "clients"
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)
#     company_id = Column(Integer, ForeignKey=("companies.id"))

#     company = relationship("Company", back_populates="clients")


class Admin(Base):
    __tablename__ = "admins"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    company = relationship("Company", back_populates='admin', uselist=False)


class HttpError(BaseModel):
    detail: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None