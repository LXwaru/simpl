from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException
from .. import models, schemas


def client_duplicate_check(db: Session, email: str, company_id: int):
    email_check = db.query(models.Client).filter(
        models.Client.email == email,
        models.Client.company_id == company_id
        ).first()
    if email_check is not None:
        return True
    return False

def create_client(
    db: Session, 
    client: schemas.ClientIn,
    company_id: int
):
    db_client = models.Client(
        full_name=client.full_name, 
        email=client.email,
        company_id=company_id)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def get_clients_by_company_id(
        db: Session,
        company_id: int
):
    client_list = db.query(models.Client).filter(models.Client.company_id == company_id).all()
    return client_list


def get_client_details(
        db: Session,
        company_id: int,
        client_id: int
):
    client = db.query(models.Client).filter(
        models.Client.id == client_id,
        models.Client.company_id == company_id).one_or_none()
    if client is None:
        raise HTTPException(status_code=404, detail='client not found')
    return client


def edit_client_info(
        db: Session,
        company_id: int,
        client_id: int,
        client_info: schemas.ClientIn
):
    client = db.query(models.Client).filter(
        models.Client.id == client_id,
        models.Client.company_id == company_id
    ).one_or_none()
    
    if client is None:
        raise HTTPException(status_code=404, detail='client not found')
    
    client.full_name = client_info.full_name
    client.email = client_info.email
    
    db.commit()
    db.refresh(client)
    return client


def delete_client(
        company_id: int,
        client_id: int, 
        db: Session
):
    client = db.query(models.Client).filter(
        models.Client.id == client_id,
        models.Client.company_id == company_id
    ).one_or_none()
    if client is None:
        raise HTTPException(status_code=404, detail='client not found')
    db.delete(client)
    db.commit()
    return {'detail': 'client deleted successfully'}