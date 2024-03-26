import uuid
from sqlalchemy import UUID, Boolean, Column, DateTime, ForeignKey, String, func
from ..database.core import Base


class MemberOffer(Base):
    """
    Represents a MemberOffer SQLAlchemy Model. Created when vendor pulishes an offer
    Association table for `many to many` relationship between offers and vendors
    """

    __tablename__ = "memberOffers"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, index=True)
    member_id = Column(UUID(as_uuid=True), index=True)
    vendor_id = Column(UUID(as_uuid=True), ForeignKey("vendors.id"), index=True)
    offer_id = Column(UUID(as_uuid=True), ForeignKey("offers.id"), index=True)
    status = Column(String(256))
    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)
    deleted = Column(Boolean, default=False)
