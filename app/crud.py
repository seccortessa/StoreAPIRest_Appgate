from sqlalchemy.orm import Session
from .              import models
from sqlalchemy     import and_
from datetime       import datetime


def check_product_id(db: Session, product_id: int):
    return db.query(models.Price).filter(models.Price.product_id == product_id).first() == None

    
def check_brand_id(db: Session, brand_id: int):
    return db.query(models.Price).filter(models.Price.brand_id == brand_id).first() == None

def check_dates(db: Session, application_date: datetime):
    return db.query(models.Price).filter(
        and_(models.Price.start_date <= application_date,models.Price.end_date >= application_date)    
    ).first() == None



def get_price(db: Session, application_date: datetime, product_id: int, brand_id: int):
    prices = db.query(models.Price).filter(
        and_(
            models.Price.start_date <= application_date,
            models.Price.end_date >= application_date,
            models.Price.product_id == product_id,
            models.Price.brand_id == brand_id            
        )
    ).order_by(models.Price.priority.desc()).first()
    return prices
    
    
    
    
