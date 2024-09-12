from sqlalchemy     import Column, Integer, String, DateTime, Float, ForeignKey
from app.database   import Base


# definitions for tables of the database as classes

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
class Brand(Base):
    __tablename__ = 'brands'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
class Price(Base):
    __tablename__ = 'prices'
    
    brand_id = Column(Integer, ForeignKey('brands(id)'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    price_list = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products(id)'))
    priority = Column(Integer)
    price = Column(Float)
    curr = Column(String(3))
    