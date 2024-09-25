from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException
from datetime import datetime, timezone

from .. import models, schemas


def create_service_item(
        db: Session,
        service_id: int,
):
    service = db.query(models.Service).filter(models.Service.id == service_id).one()
    service_item = models.ServiceItem(
        service_id = service.id,
        service_title = service.title,
        price = service.price
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
            # quantity=service_dict[service_id]
        )
        if not service_item:
            raise HTTPException(status_code=404, detail=f"Service with ID {service_id} not found")
        
        service_items.append(service_item)
    # get total price for the sale
        service = db.query(models.Service).filter(models.Service.id == service_id).one()

        amount_due += service.price

    #get client name
    client = db.query(models.Client).filter(models.Client.id == sale.client_id).one()

    new_sale = models.Sale(
        date=datetime.now(),
        client_id=sale.client_id,
        client_name=client.full_name,
        service_items=service_items,
        company_id=company_id,
        total_due=amount_due,
    )

    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)
    return new_sale