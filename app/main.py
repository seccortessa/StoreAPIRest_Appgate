from fastapi        import Depends, FastAPI
from sqlalchemy.orm import Session
from sqlalchemy     import and_
from datetime       import datetime
from app.database   import engine, Base
from app.routers    import product_router
from .              import models, schemas

# creates all the tables object for database
Base.metadata.create_all(bind=engine)

# init the API 
app = FastAPI()

# including the route for get the price data
app.include_router(product_router)

# simple root messsage
@app.get('/')
def root():
    return {"status": "API is running!", "author": "Sebastian Camilo Cortes Salazar", "message": "This project is for JR II Software Engineer's technical test at Deoxys - Appgate"}

# @app.get("/products/")
# async def read_products(db: Session = Depends(get_db)):
#     products = db.query(models.Product).all()
#     return products