from uuid import UUID
from sqlalchemy.orm import Session
from ..schema import vendor_schema
from ..model.vendor_model import Vendor

import logging

logger = logging.getLogger(__name__)  # Get logger for current module

"""
Gets a single vendor by ID
"""
def get_vendor(db: Session, id: UUID):
    vendor = db.query(Vendor).get(id)
    return vendor


"""
Gets all existing vendors -> route would not be availble to vendor, only square
"""
def get_vendors(db: Session):
    vendors = db.query(Vendor).all()
    return vendors


# create vendor
def create_vendor(db: Session, vendor: vendor_schema.VendorIn):
    db_vendor = Vendor(
        name=vendor.name, email=vendor.email, company_size=vendor.company_size
    )
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor
