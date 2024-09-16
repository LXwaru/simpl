from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from .database import SessionLocal

from .routers import (
    routers_companies,
    routers_security,
    routers_admins,
    routers_employees,
    routers_clients,
    routers_services,
    routers_sales,
    routers_appointments
)

app = FastAPI()
app.include_router(routers_admins.router, tags=["ADMINS"])
app.include_router(routers_companies.router, tags=["COMPANIES"])
app.include_router(routers_employees.router, tags=["EMPLOYEES"])
app.include_router(routers_clients.router, tags=["CLIENTS"])
app.include_router(routers_services.router, tags=["SERVICES"])
app.include_router(routers_sales.router, tags=["SALES"])
app.include_router(routers_appointments.router, tags=["APPOINTMENTS"])
app.include_router(routers_security.router, tags=["SECURITY"])

