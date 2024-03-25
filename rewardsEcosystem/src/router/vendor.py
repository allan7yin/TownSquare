from fastapi import APIRouter, Depends, HTTPException
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from src.service import vendorService
from ..database import core
from src import schema

router = APIRouter()


@router.post("/test")
def createVendor(vendor: schema.VendorCreate, db: Session = Depends(core.get_db)):
  try:
    created_vendor = vendorService.create_vendor(db=db, vendor=vendor)
    return created_vendor
  except IntegrityError:
    raise HTTPException(status_code=400, detail="Vendor email already exists")
  except Exception:
    raise HTTPException(status_code=500, detail="Internal server error")
    