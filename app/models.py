# this file is the abstraction definiction for the tables of the database

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from database import Base


# definitions for tables of the database as classes

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
class Brand(Base):
    __tablename__ = 'brand'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
class Price(Base):
    __tablename__ = 'prices'
    brand_id = Column(Integer, ForeignKey('brands(id)'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    price_list = Column(Integer)
    product_id = Column(Integer)
    priority = Column(Integer)
    price = Column(Float)
    curr = Column(String(3))
    