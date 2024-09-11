from sqlalchemy.orm import Session
from . import models

def get_price(db: Session, product_id: int, brand_id: int):
    return db.query(models.Price).filter(models.Price.product_id == product_id, models.Price.brand_id == brand_id).first()
