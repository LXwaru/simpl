from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Union, List, Optional


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


# Credit model Classes
class CreditIn(BaseModel):
    service_id: int
    client_id: int


class CreditOut(CreditIn):
    id: int
    service_title: str
    price: int
    is_redeemed: bool
    is_attached: bool
    completed_on: Optional[datetime] = None
    sale_id: int

    class Config:
        from_attributes = True


# Appointment Model Classes
class AppointmentIn(BaseModel):
    client_id: int
    service_id: int
    employee_id: int
    credit_id: Optional[int] = None
    start_time: datetime


class AppointmentOut(AppointmentIn):
    id: int
    company_id: int
    is_confirmed: bool
    end_time: datetime
    credit: Optional[CreditOut] = None
    is_complete: bool

    class Config:
        from_attributes=True


# Sale Model Classes
class SaleIn(BaseModel):
    client_id: int
    service_ids: List[int]


class SaleOut(BaseModel):
    id: int
    company_id: int
    company_name: str
    date: datetime
    client_id: int
    client_name: str
    total_due: int
    credits: List[CreditOut]

    class Config:
        from_attributes = True


# Client Model Classes
class ClientIn(BaseModel):
    full_name: str
    email: str


class ClientOut(ClientIn):
    id: int
    company_id: int
    credits: list[CreditOut] = []
    appointments: list[AppointmentOut] = []
    sales: list[SaleOut] = []

    class Config:
        from_attributes = True


# # Employee Model Classes
class PayRateIn(BaseModel):
    employee_id: int
    service_id: int
    rate_per_service: Union[int, None] = None

class PayRateOut(PayRateIn):
    id: int
    company_id: int

    class Config:
        from_attributes = True

class EmployeeIn(BaseModel):
    full_name: str
    email: str


class EmployeeOut(EmployeeIn):
    id: int
    company_id: int
    is_active: bool
    appointments: list[AppointmentOut] = []
    pay_rates: list[PayRateOut] = []

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
