from datetime import timedelta, datetime
from typing import List, Optional, Literal
from uuid import UUID
from pydantic import BaseModel
from ..enums import OFFER_TYPES

class OfferIn(BaseModel):
  """
  Represents an Offer Pydantic Schema for Request Body
  """
  startDate: Optional[datetime] = datetime.now()
  endDate: Optional[datetime] = datetime.now() + timedelta(days=1)
  description: Optional[str] = None
  termsAndConditions: Optional[str] = None
  offerType: Literal[OFFER_TYPES.cash_back, OFFER_TYPES.discount, OFFER_TYPES.points]

  
class OfferOut(BaseModel):
  """
  Represents an Offer Pydantic Schema for Response Body
  """
  id: UUID
  startDate: datetime
  endDate: datetime
  description: Optional[str] = None
  termsAndConditions: Optional[str] = None
  offerType: Literal[OFFER_TYPES.cash_back, OFFER_TYPES.discount, OFFER_TYPES.points]
  isPublished: bool

class OfferListOut(BaseModel):
  """
  Represents an List of Offer Pydantic Schema for Response Body
  """
  vendors: List[OfferOut]