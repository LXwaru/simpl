from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from .. import schemas, utils_db
from ..crud import crud_admins
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/api/admins/", response_model=schemas.AdminOut)
def create_admin(
    admin: schemas.AdminCreate, 
    db: Session = Depends(utils_db.get_db)
):
    db_admin = crud_admins.get_admin_by_username(db, username=admin.username)
    if db_admin:
        raise HTTPException(status_code=400, detail="username already registered")
    return crud_admins.create_admin(db=db, admin=admin)


@router.get("/api/admins/", response_model=list[schemas.AdminOut])
def list_admins(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(utils_db.get_db)
):
    admins = crud_admins.get_admins(db, skip=skip, limit=limit)
    return admins