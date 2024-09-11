from pydantic import BaseModel
from datetime import datetime

class PriceBase(BaseModel):
    brand_id: int
    start_date: datetime
    end_date: datetime
    price_list: int
    product_id: int
    priority: int
    price: float
    curr: str
    
class PriceCreate(BaseModel):
    pass

class PriceOut(BaseModel):
    class Config:
        orm_model = True