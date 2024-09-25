from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, TIMESTAMP, Numeric, Interval, func, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List
from pydantic import BaseModel
from datetime import datetime, timezone
from .database import Base
import pytz


def utc_now():
    return datetime.now(pytz.utc)


# sale_service_association = Table(
#     'sale_service', Base.metadata,
#     Column('sale_id', Integer, ForeignKey('sales.id')),
#     Column('sale_item_id', Integer, ForeignKey('sale_items.id'))
# )

# class SaleServiceAssociation(Base):
#     __tablename__ = 'sale_service_association'
#     sale_id: Mapped[int] = mapped_column(ForeignKey('sales.id'), primary_key=True)
#     sale_item_id: Mapped[int] = mapped_column(ForeignKey('sale_items.id'))
#     sale_item: Mapped['SaleItem'] = relationship()


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, index=True)
    admin_id = Column(Integer, ForeignKey("admins.id"))

    admin = relationship("Admin", back_populates="company")
    employees = relationship("Employee", back_populates="company", cascade='all, delete')
    clients = relationship("Client", back_populates="company", cascade='all, delete')
    services = relationship("Service", back_populates="company", cascade="all, delete")
    sales = relationship("Sale", back_populates='company', cascade='all, delete')
    # appointments = relationship("Appointment", back_populates='company', cascade='all, delete')


class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="employees")


class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="clients")
    credits = relationship("Sale", back_populates="client")


class Admin(Base):
    __tablename__ = "admins"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    company = relationship("Company", back_populates='admin', uselist=False)


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    price = Column(Numeric, index=True)
    description = Column(String, index=True)
    duration = Column(Interval)
    is_enabled = Column(Boolean, default=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="services")
    service_items = relationship("ServiceItem", back_populates="service")


class ServiceItem(Base):
    __tablename__ = "service_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    service_id = Column(Integer, ForeignKey('services.id'))
    service_title = Column(String, index=True)
    price = Column(Integer, index=True)
    sale_id = Column(Integer, ForeignKey('sales.id'))
    sales = relationship('Sale', back_populates='service_items')

    service = relationship("Service", back_populates='service_items')



class Sale(Base):
    __tablename__= "sales"
    
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    date = Column(TIMESTAMP(timezone=True), default=utc_now)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client_name = Column(String, index=True)
    total_due = Column(Numeric, index=True)
    is_paid = Column(Boolean, default=False)
    service_items: Mapped[List["ServiceItem"]] = relationship(back_populates='sales')

    company = relationship("Company", back_populates="sales")
    client = relationship("Client", back_populates="credits")
    


# class Appointment(Base):
#     __tablename__ = "appointments"

#     id = Column(Integer, primary_key=True)
#     company_id = Column(Integer, ForeignKey('companies.id'))
#     service_id = Column(Integer, ForeignKey('services.id'))
#     client_id = Column(Integer, ForeignKey('clients.id'))
#     employee_id = Column(Integer, ForeignKey('employees.id'))
#     start_time = Column(DateTime, index=True)
#     location = Column(String, index=True)
#     is_confirmed = Column(Boolean, default=False)

#     company = relationship("Company", back_populates="appointments")


class HttpError(BaseModel):
    detail: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None