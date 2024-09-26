from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from .. import schemas, utils_db
from ..crud import crud_clients
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/api/{company_id}/clients', response_model=schemas.ClientOut)
def create_client(
    company_id: int,
    client: schemas.ClientIn,
    db: Session = Depends(utils_db.get_db)
):
    db_client = crud_clients.get_client_by_email(db, email=client.email)
    if db_client:
        raise HTTPException(status_code=400, detail="client is already in database")
    return crud_clients.create_client(db=db, client=client, company_id=company_id)


@router.get('/api/{company_id}/clients', response_model=list[schemas.ClientOut])
def list_clients(
    company_id: int, 
    db: Session = Depends(utils_db.get_db)
):
    clients = crud_clients.get_clients_by_company_id(db=db, company_id=company_id)
    return clients