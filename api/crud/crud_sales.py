from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException
from datetime import datetime, timezone

from .. import models, schemas


def create_sale(
        db: Session, 
        company_id: int,
        sale: schemas.SaleIn
) -> schemas.SaleOut:
    
    # getting the amount du
    service_prices = []
    for service_id in sale.service_ids:
        service = db.query(models.Service).filter(models.Service.id == service_id).one()

        if not service:
            raise HTTPException(status_code=404, detail=f"Service with ID {service_id} not found")
        
        service_prices.append(service)
        
    amount_due = sum(service.price for service in service_prices)

    # getting the services in the list
    # services = {}
    # for service in sale.service_ids:
    #     services[price] = 

    new_sale = models.Sale(
        date=sale.date,
        client_id=sale.client_id,
        company_id=company_id,
        total_due=amount_due
    )

    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)

    for service in services:
        db.execute(
            models.sale_service_association.insert().values(
                sale_id=new_sale.id,
                service_id=service.id
            )
        )
    db.commit()
    db.refresh(new_sale)
    return new_sale