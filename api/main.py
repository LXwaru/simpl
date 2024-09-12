from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from .database import SessionLocal

from . import (
    routers_companies,
    routers_security,
    routers_admins,
    routers_employees
)

app = FastAPI()
app.include_router(routers_companies.router, tags=["COMPANIES"])
app.include_router(routers_security.router, tags=["SECURITY"])
app.include_router(routers_admins.router, tags=["ADMINS"])
app.include_router(routers_employees.router, tags=["EMPLOYEES"])