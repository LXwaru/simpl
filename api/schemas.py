from pydantic import BaseModel
from datetime import datetime
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


# # Client Model Classes
# class ClientIn(BaseModel):
#     name: str
#     email: str


# class ClientOut(ClientIn):
#     id: int
#     company_id: int

#     class Config:
#         from_attributes = True


# # Employee Model Classes
class EmployeeIn(BaseModel):
    full_name: str
    company_id: int



class EmployeeOut(EmployeeIn):
    id: int

    class Config:
        from_attribute = True


# Service Model Classes


# Appointment Model Classes


# Sale Model Classes


# Company Model Classes
class CompanyIn(BaseModel):
    name: str
    description: Union[str, None] = None


class CompanyOut(CompanyIn):
    id: int
    admin_id: int
    # admins: list[AdminOut] = []
    # clients: list[ClientOut] = []
    employees: list[EmployeeOut] = []
    # appointments: list[AppointmentOut] = []
    # sales: list[SaleOut] = []


    class Config:
        from_attributes = True