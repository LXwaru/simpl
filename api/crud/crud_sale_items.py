from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException, Depends
from datetime import datetime, timezone

from .. import models, schemas


def create_sale_item(
        db: Session,
        company_id: int,
        sale_item: schemas.SaleItemIn
) -> schemas.SaleItemOut:
    db_sale_item = models.SaleItem(
        service_id=sale_item.service_id,
        company_id=company_id
    )
    db.add(db_sale_item)
    db.commit()
    db.refresh(db_sale_item)
    return db_sale_item
