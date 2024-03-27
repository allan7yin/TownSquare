from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from ..service import vendor_service
from ..database import core
from ..schema import vendor_schema

router = APIRouter(
    prefix="/vendors",
    tags=["vendors"],
    responses={404: {"description": "Not found"}},
)


# get vendor endpoint by vendor id
@router.get("/{id}", response_model=vendor_schema.VendorOut)
async def getVendor(id: UUID, db: Session = Depends(core.get_db)):
    try:
        vendor = vendor_service.get_vendor(db=db, id=id)
        return vendor
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


# get all vendors
@router.get("/", response_model=vendor_schema.VendorListOut)
async def getVendors(db: Session = Depends(core.get_db)):
    try:
        vendors = vendor_service.get_vendors(db=db)
        return vendors
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


# patch a vendor -> do this later
# @router.patch("/{id}")
# def patchVendor(id: UUID, db: Session = Depends(core.get_db)):
#     try:


# create vendor endpoint
@router.post("/", response_model=vendor_schema.VendorOut)
async def createVendor(vendor: vendor_schema.VendorIn, db: Session = Depends(core.get_db)):
    try:
        created_vendor = vendor_service.create_vendor(db=db, vendor=vendor)
        return created_vendor
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Vendor email already exists")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
