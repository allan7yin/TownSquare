import uuid
from sqlalchemy import UUID, Boolean, Column, DateTime, String, Text, func
from ..database.core import Base


class Offer(Base):
    """
    Represents an Offer construct SQLAlchemy Model
    """
    __tablename__ = "offers"
    id = Column(UUID, primary_key=True, default=uuid.uuid4, index=True)  # Corrected UUID usage
    startDate = Column(DateTime, default=func.now(), nullable=False)
    endDate = Column(DateTime, default=func.now(), nullable=False)
    termsAndConditions = Column(Text(2048), nullable=True)
    offerType = Column(String(256), nullable=False, index=True)
    isPublished = Column(Boolean, index=True)
    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)
