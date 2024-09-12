from sqlalchemy.orm import Session
from .              import models
from sqlalchemy     import and_
from datetime       import datetime




def get_price(db: Session, application_date: datetime, product_id: int, brand_id: int):
    prices = db.query(models.Price).filter(
        and_(
            models.Price.start_date <= application_date,
            models.Price.end_date >= application_date,
            models.Price.product_id == product_id,
            models.Price.brand_id == brand_id            
        )
    ).order_by(models.Price.priority.desc()).first()
    if prices:
    
        return {
            "product_id": prices.product_id,
            "brand_id": prices.brand_id,
            "price_list": prices.price_list,
            "start_date": prices.start_date,
            "end_date": prices.end_date,
            "price_type": prices.price,
            "currency": prices.curr
        }
    else:
        return {"error": "No price found for the specified parameters"}
    
    
    
    
