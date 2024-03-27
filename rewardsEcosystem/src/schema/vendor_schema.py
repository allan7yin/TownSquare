from typing import List
from uuid import UUID
from pydantic import BaseModel

class VendorIn(BaseModel):
  """
  Represents a Square Vendor Pydantic Schema for Request Body
  """
  name: str
  email: str
  company_size: int

class VendorOut(BaseModel):
  """
  Represents a Square Vendor Pydantic Schema for Response Body
  """
  id: UUID
  name: str
  email: str
  company_size: int

class VendorListOut(BaseModel):
  """
  Represents a List of Square Vendor Pydantic Schema for Response Body
  """
  vendors: List[VendorOut]