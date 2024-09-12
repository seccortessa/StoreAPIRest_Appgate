# import pytest
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.main import app
# from app.database import Base
# from app.dependencies import get_db
# from app.models import Product, Price, Brand
# from datetime import datetime

# # create a test database
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Fixture para sobreescribir la base de datos en cada prueba
# @pytest.fixture(scope="function")
# def db_session():
#     Base.metadata.create_all(bind=engine)
#     db = TestingSessionLocal()
#     try:
#         # these are test data
#         product = Product(id=35455, name="Product1")
#         db.add(product)
        
#         brand = Brand(id=1, name="Brand1")
#         db.add(brand)

#         price = Price(
#             brand_id=1, 
#             start_date=datetime(2020, 6, 14), 
#             end_date=datetime(2020, 12, 31), 
#             price_list=1, 
#             product_id=35455, 
#             priority=0,
#             price=32.5, 
#             curr = 'USD'
#         )
#         db.add(price)
#         db.commit()
#         yield db
#     finally:
#         db.close()
#         Base.metadata.drop_all(bind=engine)

# # Fixture para usar TestClient en FastAPI
# @pytest.fixture(scope="module")
# def client():
#     def override_get_db():
#         db = TestingSessionLocal()
#         try:
#             yield db
#         finally:
#             db.close()

#     app.dependency_overrides[get_db] = override_get_db
#     with TestClient(app) as c:
#         yield c
