from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from .. import schemas, utils_db, utils_sec
from ..crud import crud_admins
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    return crud_admins.get_admins(db=db)


@router.get("/api/admin/{admin_id}/", response_model=schemas.AdminOut)
def get_admin_by_id(
    admin_id: int,
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    return crud_admins.get_admin(db, admin_id=admin_id)


@router.put("/api/admin/{admin_id}/", response_model=schemas.AdminOut)
def toggle_activation_status_admin(
    admin_id: int,
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    return crud_admins.toggle_activation_status_admin(db=db, admin_id=admin_id)


@router.delete("/api/admin/{admin_id}/")
def delete_admin(
    admin_id: int,
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    return crud_admins.delete_admin(db=db, admin_id=admin_id)


@router.post('/api/logout/')
def logout(response: Response):
    response.delete_cookie('access_token')
    return {'message': 'logout successful'}