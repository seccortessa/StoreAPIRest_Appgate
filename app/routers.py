from fastapi            import  APIRouter, Depends, HTTPException
from sqlalchemy.orm     import  Session
from app                import  crud, schemas
from app.dependencies   import  get_db
from datetime           import datetime

product_router = APIRouter()

@product_router.get("/price/", response_model=schemas.PriceBase)

# function to get the price 
async def read_price(application_date: datetime, product_id: int, brand_id: int, db: Session = Depends(get_db)):
    
    # check if either entered price id, product ir or date is in the prices table 
    if (crud.check_product_id(db, product_id)) or (crud.check_brand_id(db, brand_id)):
        raise HTTPException(status_code=404, detail=f"Parameter(s) not found: {'product_id' if crud.check_product_id(db, product_id) else ''}{', ' if crud.check_product_id(db, product_id) and crud.check_brand_id(db, brand_id) else ''}{'brand_id' if crud.check_brand_id(db, brand_id) else ''}")
        
    if crud.check_dates(db, application_date):
        raise HTTPException(status_code=404, detail="Entered date out of range")
    
    #  return if all data is correct        # 
    return (crud.get_price(db, application_date, product_id, brand_id))
