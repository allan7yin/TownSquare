from typing import List
from uuid import UUID
from pydantic import BaseModel

class MemberOfferIn(BaseModel):
  """
  Represents a Member Offer Pydantic Schema for Request Body
  """
  vendor_ids: List[UUID]
  offer_id: UUID

class MemberOfferOut(BaseModel):
  """
  Represents a Member Offer Pydantic Schema for Response Body
  """
  id: UUID
  vendor_ids: List[UUID]
  offer_id: UUID

class MemberOfferListOut(BaseModel):
  """
  Represents a List of Member Offer Pydantic Schema for Response Body
  """
  vendors: List[MemberOfferOut]