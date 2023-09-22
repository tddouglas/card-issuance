import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

print(f"Starting up DB - {os.getenv('SQLLLIGHT_DATABASE_URL')}")

# connect_args only needed for sqlite
engine = create_engine(
    # os.getenv('SQLALCHEMY_DATABASE_URL')  # SQL Alchemy
    os.getenv('SQLLLIGHT_DATABASE_URL'), connect_args={"check_same_thread": False}  # SQL Light DB
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
