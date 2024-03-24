from enum import Enum

class BaseEnum(str, Enum):
    def __str__(self) -> str:
        return str.__str__(self)
    
class OFFER_TYPES(BaseEnum):
    cash_back = "cash_back"
    points = "points"
    discount = "discount"

class MEMBER_TIER(BaseEnum):
    entry = "entry"
    plus = "plus"
    premium = "premium"