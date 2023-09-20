from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# todo make this a environment variable
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db" <-- use this line for sqlite db
SQLALCHEMY_DATABASE_URL = "postgresql://sebastianl@127.0.0.1/sebastianl"

# connect_args only needed for sqlite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    #  SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}<--exchange previous line by this for sqlite db
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
