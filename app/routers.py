from fastapi            import  APIRouter, Depends, HTTPException
from sqlalchemy.orm     import  Session
from app                import  crud, schemas
from app.dependencies   import  get_db
from datetime           import datetime

product_router = APIRouter()

@product_router.get("/price/")

async def read_price(application_date: datetime, product_id: int, brand_id: int, db: Session = Depends(get_db)):
    price = crud.get_price(db, application_date, product_id, brand_id)
    if not price:
        raise HTTPException(status_code=404, detail="No price found for the given parameters")
    return price