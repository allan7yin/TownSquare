from sqlalchemy.orm import Session
from .. import schema
from ..model.vendor import Vendor
import uuid

def createVendor(db: Session, vendor: schema.VendorCreate):
  vendorId = uuid.uuid4()
  db_vendor = Vendor(vendor)
  db.add(db_vendor)
  db.commit()
  db.refresh(db_vendor)
  return db_vendor