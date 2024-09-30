from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Union, List, Optional



# Appointment Model Classes
class AppointmentIn(BaseModel):
    client_id: int
    service_id: int
    employee_id: int
    start_time: datetime


class AppointmentOut(AppointmentIn):
    id: int
    company_id: int
    is_confirmed: bool
    is_paid: bool
    is_complete: bool

    class Config:
        from_attributes=True


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


# SaleItem model Classes
class SaleItemIn(BaseModel):
    service_id: int


class SaleItemOut(SaleItemIn):
    id: int
    service_title: str
    price: int

    class Config:
        from_attributes = True


# Sale Model Classes
class SaleIn(BaseModel):
    client_id: int
    service_ids: List[int]


class SaleOut(BaseModel):
    id: int
    company_id: int
    date: datetime
    client_id: int
    total_due: int
    is_paid: bool
    service_items: List[SaleItemOut]

    class Config:
        from_attributes = True


# Client Model Classes
class ClientIn(BaseModel):
    full_name: str
    email: str


class ClientOut(ClientIn):
    id: int
    company_id: int
    credits: list[SaleItemOut] = []
    appointments: list[AppointmentOut] = []

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


# Company Model Classes
class CompanyIn(BaseModel):
    name: str
    description: Union[str, None] = None


class CompanyOut(CompanyIn):
    id: int
    admin_id: int
    appointments: list[AppointmentOut] = []
    clients: list[ClientOut] = []
    employees: list[EmployeeOut] = []
    services: list[ServiceOut] = []
    sales: list[SaleOut] = []


    class Config:
        from_attributes = True


        # Admin Model Classes
class AdminIn(BaseModel):
    username: str


class AdminCreate(AdminIn):
    password: str


class AdminOut(AdminIn):
    id: int
    is_active: bool
    company: Optional[CompanyOut]

    class Config:
        from_attributes = True