from sqlalchemy import UUID, Boolean, Column, DateTime, String, Text, func
from sqlalchemy.orm import relationship
from ..database.core import Base

import uuid

class Offer(Base):
    """
    Represents an Offer construct SQLAlchemy Model
    """

    __tablename__ = "offers"
    id = Column(
        UUID, primary_key=True, default=uuid.uuid4, index=True
    )  # Corrected UUID usage
    startDate = Column(DateTime, default=func.now(), nullable=False)
    endDate = Column(DateTime, default=func.now() + func.interval('1 day'), nullable=False)
    description = Column(Text(2048), nullable=True)
    termsAndConditions = Column(Text(2048), nullable=True)
    offerType = Column(String(256), nullable=False, index=True)
    isPublished = Column(Boolean, default=False,index=True)

    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)
    deleted = Column(Boolean, default=False)

    # define relationships with other tables 
    member_offers = relationship("MemberOffer", backref="Offer", cascade="all, delete-orphan")
