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

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response