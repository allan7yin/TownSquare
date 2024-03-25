from sqlalchemy import create_engine, Column, DateTime, func, UUID
from sqlalchemy.orm import sessionmaker
import uuid

import typing as t
from sqlalchemy.ext.declarative import declarative_base

# from ..config import SQLALCHEMY_DATABASE_URI

# engine = create_engine(SQLALCHEMY_DATABASE_URI)  # Uncomment this when using the config variable
engine = create_engine("postgresql://dev:password@localhost:5432/dev")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()