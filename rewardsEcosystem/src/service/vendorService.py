from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from .. import schema
from ..model.vendor import Vendor
import uuid
import logging

logger = logging.getLogger(__name__)  # Get logger for current module

def create_vendor(db: Session, vendor: schema.VendorCreate):
  vendorId = uuid.uuid4()
  try:
    db_vendor = Vendor(name=vendor.name, email=vendor.email, company_size=vendor.company_size)
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor
  except IntegrityError as e:
    logger.error(f"Error creating vendor: {e}")
    raise
  except Exception as e:
    logger.exception(f"Unexpected error: {e}")
    raise

  
  
