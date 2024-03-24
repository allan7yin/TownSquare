from sqlalchemy import UUID, Column, ForeignKey, String
from ..database.core import Base

class MemberOffer(Base):
    """
    Represents a MemberOffer SQLAlchemy Model. Created when vendor pulishes an offer
    Association table for `many to many` relationship between offers and vendors
    """
    __tablename__ = "memberOffers"
    member_id = Column(UUID(as_uuid=True)) # if we have members table, would be foreign key, but we get this through API call to Square
    vendor_id = Column(UUID(as_uuid=True), ForeignKey("vendors.id"))
    offer_id = Column(UUID(as_uuid=True), ForeignKey("offers.id"))
    status = Column(String(256))
