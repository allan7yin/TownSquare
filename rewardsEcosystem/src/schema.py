from pydantic import BaseModel

class VendorCreate(BaseModel):
    """
    Represents a Square Vendor Pydantic Schema
    """
    name: str
    email: str
    company_size: int
