from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from .dependencies import get_query_token
from .internal import admin
from .router import items, users
from .service import vendorService
from .database import core
from .. import schema

app = FastAPI(dependencies=[Depends(get_query_token)])

# Dependency
def get_db():
    db = core.SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(users.router)
app.include_router(items.router)
app.include_router(admin.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

@app.get("/test")
def testDatabaseConnection(vendor: schema.VendorCreate, db: Session = Depends(get_db)):
    vendorService.createVendor(db=db, vendor=vendor)
    
    

