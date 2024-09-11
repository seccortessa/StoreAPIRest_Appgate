from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import datetime

from . import models, schemas
from app.database import engine, Base, get_db

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/products/")
async def read_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

# endpoint for get the price
@app.get("/price/")
# in this function we apply the logic in order to get the correct price applicable for the product and datetime entered
async def get_price(application_date: datetime, product_id: int, brand_id: int, db: Session = Depends(get_db)):
    prices = db.query(models.Price).filter(
        and_(
            models.Price.start_date <= application_date,
            models.Price.end_date >= application_date,
            models.Price.product_id == product_id,
            models.Price.brand_id == brand_id            
        )
    ).order_by(models.Price.priority.desc()).first()
    # takes the first result, since it is ordered by priority
    
    
    # organize and present the desired results
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
    