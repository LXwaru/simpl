from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException
from datetime import datetime, timezone

from .. import models, schemas


def create_service_item(
        db: Session,
        service_id: int,
        client_id: int
):
    service = db.query(models.Service).filter(models.Service.id == service_id).one_or_none()
    if service is None:
        return None
    service_item = models.ServiceItem(
        service_id = service.id,
        service_title = service.title,
        price = service.price,
        client_id = client_id
    )
    db.add(service_item)
    db.commit()
    db.refresh(service_item)
    return service_item


def create_sale(
        db: Session, 
        company_id: int,
        sale: schemas.SaleIn 
) -> schemas.SaleOut:

    # get a list of services
    service_items = []
    amount_due = 0
    for service_id in sale.service_ids:
        service_item = create_service_item( 
            db=db,
            service_id=service_id,
            client_id = sale.client_id
        )
        if service_item is None:
            raise HTTPException(status_code=404, detail=f"Service with ID {service_id} not found")
        
        service_items.append(service_item)
    # get total price for the sale
        service = db.query(models.Service).filter(
            models.Service.id == service_id,
            models.Service.company_id == company_id
        ).one_or_none()

        amount_due += service.price

    #get client name
    client = db.query(models.Client).filter(models.Client.id == sale.client_id).one_or_none()
    if client is None:
        raise HTTPException(status_code=404, detail='client not found')

    company = db.query(models.Company).filter(models.Company.id == company_id).one_or_none()
    if company is None:
        raise HTTPException(status_code=404, detail='company not found')
    
    new_sale = models.Sale(
        date=datetime.now(),
        client_id=sale.client_id,
        client_name=client.full_name,
        service_items=service_items,
        company_id=company_id,
        company_name=company.name,
        total_due=amount_due,
    )

    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)
    return new_sale


def list_sales(
    db: Session,
    company_id: int
):
    return db.query(models.Sale).filter(models.Sale.company_id == company_id).all()


def get_sale(
        db: Session,
        company_id: int,
        sale_id: int
):
    sale = db.query(models.Sale).filter(
        models.Sale.id == sale_id,
        models.Sale.company_id == company_id
    ).one_or_none()

    if sale is None:
        return None
    
    return sale


def deem_sale_paid(
        db: Session,
        company_id: int,
        sale_id: int
):
    sale = db.query(models.Sale).filter(
        models.Sale.id == sale_id,
        models.Sale.company_id == company_id
    ).one_or_none()
    
    if sale is None:
        return None

    sale.is_paid = True

    db.query(models.ServiceItem).filter(
        models.ServiceItem.sale_id == sale_id,
    ).update({'is_active': True})

    
    db.commit()
    db.refresh(sale)
    return sale


def delete_sale(
    db: Session,
    company_id: int,
    sale_id: int
):
    sale = db.query(models.Sale).filter(
        models.Sale.id == sale_id,
        models.Sale.company_id == company_id
    ).one_or_none()

    if sale is None:
        raise HTTPException(status_code=404, detail='sale not found')
    db.delete(sale)
    db.commit()

    return {'detail': 'sale deleted successfully'}