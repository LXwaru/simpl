from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Union, List, Optional


# Admin Model Classes
class AdminIn(BaseModel):
    username: str


class AdminCreate(AdminIn):
    password: str


class AdminOut(AdminIn):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


# Client Model Classes
class ClientIn(BaseModel):
    full_name: str
    email: str


class ClientOut(ClientIn):
    id: int
    company_id: int

    class Config:
        from_attributes = True


# # Employee Model Classes
class EmployeeIn(BaseModel):
    full_name: str
    email: str



class EmployeeOut(EmployeeIn):
    id: int
    company_id: int
    is_active: bool

    class Config:
        from_attribute = True


# Service Model Classes
class ServiceIn(BaseModel):
    title: str
    price: int
    duration: timedelta
    description: str


class ServiceOut(ServiceIn):
    id: int
    company_id: int
    is_enabled: bool

    class Config:
        from_attributes = True


# Appointment Model Classes
# class AppointmentIn


# Sale Model Classes
class SaleIn(BaseModel):
    date: datetime
    client_id: int
    services: list[ServiceOut]


class SaleOut(SaleIn):
    id: int
    company_id: int
    total_due: int

    class Config:
        from_attributes = True

# Company Model Classes
class CompanyIn(BaseModel):
    name: str
    description: Union[str, None] = None


class CompanyOut(CompanyIn):
    id: int
    admin_id: int
    clients: list[ClientOut] = []
    employees: list[EmployeeOut] = []
    # appointments: list[AppointmentOut] = []
    sales: list[SaleOut] = []


    class Config:
        from_attributes = True