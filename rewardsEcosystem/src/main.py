from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .internal import admin
from .router import items, users, vendor
from .service import vendorService
from . import schema
from sqlalchemy.exc import IntegrityError


import logging

from .database.core import Base, engine
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
app.include_router(admin.router)
app.include_router(vendor.router)


@app.get("/")
async def root():
  return {"message": "Hello Bigger Applications!"}
