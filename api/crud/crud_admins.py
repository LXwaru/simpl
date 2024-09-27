from sqlalchemy.orm import Session
from .. import models, schemas, utils_sec
from sqlalchemy.exc import NoResultFound


def get_admin(db: Session, admin_id: int):
    return db.query(models.Admin).filter(models.Admin.id == admin_id).first()


def get_admin_by_username(
    db: Session, 
    username: str
):
    return db.query(models.Admin).filter(models.Admin.username == username).first()


def get_admins(
        db: Session, 
        skip: int = 0, 
        limit: int = 10
):
    return db.query(models.Admin).offset(skip).limit(limit).all()


def create_admin(
        db: Session, 
        admin: schemas.AdminIn
):
    hashed_password = utils_sec.get_password_hash(admin.password)
    db_admin = models.Admin(username=admin.username, hashed_password=hashed_password)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


def toggle_activation_status_admin(
        db: Session,
        admin_id: int,
):
    try:
        admin = db.query(models.Admin).filter(models.Admin.id == admin_id).one()
        if admin.is_active:
            admin.is_active = False
        else:
            admin.is_active = True
        db.commit()
        db.refresh(admin)
        return admin
    except NoResultFound:
        db.rollback()
        return {'detail': 'no admin with that id'}
    

def delete_admin(
        db: Session,
        admin_id: int
):
    try:
        admin = db.query(models.Admin).filter(models.Admin.id == admin_id).one()
        db.delete(admin)
        db.commit()
        return {'detail': "Admin deleted"}
    except NoResultFound:
        return {'detail': 'admin not found'}