from pydantic import BaseModel
from datetime import datetime

class PriceBase(BaseModel):
    product_id: int
    brand_id: int
    price_list: int
    start_date: datetime
    end_date: datetime
    price: float
    class Config:
        orm_model = True