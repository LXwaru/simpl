from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, TIMESTAMP, Numeric, Interval, func, Table, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List
from pydantic import BaseModel
from datetime import datetime, timezone
from .database import Base
import pytz


def utc_now():
    return datetime.now(pytz.utc)


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
    appointments = relationship("Appointment", back_populates='company', cascade='all, delete')
    pay_rates = relationship("PayRate", back_populates='company', cascade='all, delete')


class PayRate(Base):
    __tablename__ = "pay_rates"
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    rate_per_service = Column(Numeric)
    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship("Company", back_populates="pay_rates")
    service = relationship("Service", back_populates="pay_rates")
    employee = relationship("Employee", back_populates="pay_rates")


class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="employees")
    appointments = relationship('Appointment', back_populates='employee')
    pay_rates = relationship("PayRate", back_populates='employee')


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
    __table_args__ = (
        UniqueConstraint('title', 'company_id'),
    )

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    price = Column(Numeric, index=True, nullable=False)
    description = Column(String, index=True)
    duration = Column(Interval, nullable=False)
    is_enabled = Column(Boolean, default=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    company = relationship("Company", back_populates="services")
    service_items = relationship("ServiceItem", back_populates="service")
    pay_rates = relationship("PayRate", back_populates="service")


class Client(Base):
    __tablename__ = "clients"
    __table_args__ = (
        UniqueConstraint('email', 'company_id'),
    )
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=False, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="clients")
    credits = relationship("ServiceItem", back_populates="client")
    sales = relationship('Sale', back_populates='client')
    appointments = relationship('Appointment', back_populates='client')


class ServiceItem(Base):
    __tablename__ = "service_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    service_id = Column(Integer, ForeignKey('services.id'))
    service_title = Column(String, index=True)
    price = Column(Integer, index=True)
    # is_active is False until sale.is_paid = True
    is_active = Column(Boolean, default=False)
    # is_redeemed is False until the service_item's is_completed date
    is_redeemed = Column(Boolean, default=False)
    # completed_on is a nullable field that is filled with a datetime when the service_item is completed
    completed_on = Column(DateTime(timezone=True), nullable=True)
    sale_id = Column(Integer, ForeignKey('sales.id'))
    client_id = Column(Integer, ForeignKey('clients.id'))
    sale = relationship('Sale', back_populates='service_items')
    client = relationship('Client', back_populates='credits')
    service = relationship("Service", back_populates='service_items')



class Sale(Base):
    __tablename__= "sales"
    
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    company_name = Column(String, index=True)
    date = Column(TIMESTAMP(timezone=True))
    client_id = Column(Integer, ForeignKey("clients.id"))
    client_name = Column(String, index=True)
    total_due = Column(Numeric, index=True)
    service_items: Mapped[List["ServiceItem"]] = relationship(back_populates='sale')

    company = relationship("Company", back_populates="sales")
    client = relationship("Client", back_populates="sales")
    

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    employee_id = Column(Integer, ForeignKey('employees.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    start_time = Column(DateTime, index=True)
    is_confirmed = Column(Boolean, default=False)
    has_credit = Column(Boolean, default=False)
    is_complete = Column(Boolean, default=False)

    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship("Company", back_populates="appointments")
    client = relationship('Client', back_populates='appointments')
    employee = relationship('Employee', back_populates='appointments')


class HttpError(BaseModel):
    detail: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None