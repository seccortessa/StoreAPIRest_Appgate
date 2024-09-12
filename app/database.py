from sqlalchemy                 import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm             import sessionmaker, declarative_base
from data                       import DATABASE_NAME


# url for the connection to the database
SQLALCHEMY_DATABASE_URL = f"sqlite:///./{DATABASE_NAME}"

# print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# create the session to inteact woth the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

