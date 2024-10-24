from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
    Cookie
)
from .. import schemas, utils_db, utils_sec
from ..crud import crud_clients
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()


@router.post('/api/clients/{company_id}/', response_model=schemas.ClientOut)
def create_client(
    company_id: int,
    client: schemas.ClientIn,
    db: Session = Depends(utils_db.get_db),
    access_token: str = Cookie(None)
):
    duplicate = crud_clients.client_duplicate_check(db, email=client.email, company_id=company_id)
    if duplicate:
        raise HTTPException(status_code=400, detail="client is already in database")
    return crud_clients.create_client(db=db, client=client, company_id=company_id)


@router.get('/api/clients/{company_id}/', response_model=list[schemas.ClientOut])
def list_clients(
    company_id: int, 
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    clients = crud_clients.get_clients_by_company_id(db=db, company_id=company_id)
    return clients


@router.get('/api/client/{company_id}/{client_id}/', response_model=schemas.ClientOut)
def get_client_details(
    company_id: int,
    client_id: int,
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    return crud_clients.get_client_details(db=db, company_id=company_id, client_id=client_id)


@router.put('/api/client/{company_id}/{client_id}/', response_model=schemas.ClientOut)
def edit_client_info(
    company_id: int,
    client_id: int,
    client_info: schemas.ClientIn,
    db: Session = Depends(utils_db.get_db),
    access_token: str = Cookie(None)
):
    return crud_clients.edit_client_info(
        db=db,
        company_id=company_id, 
        client_id=client_id, 
        client_info=client_info
    )


@router.delete('/api/client/{company_id}/{client_id}')
def delete_client(
    company_id: int,
    client_id: int,
    db: Session = Depends(utils_db.get_db),
    token: str = Depends(oauth2_scheme)
):
    return crud_clients.delete_client(db=db, company_id=company_id, client_id=client_id)


