from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import models, schemas
from database import engine, Base, get_db

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/products/")
def read_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products
