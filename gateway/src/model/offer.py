from sqlalchemy import Column, DateTime, String, Text, func, Boolean
from ..database.core import Base

class Offer(Base):
    """
    Represents an Offer construct SQLAlchemy Model
    """
    __tablename__ = "offers"
    startDate = Column(DateTime, default=func.now(), nullable=False)
    endDate = Column(DateTime, default=func.now(), nullable=False)
    termsAndConditions = Column(Text(2048), nullable=True)
    offerType = Column(String(256), nullable=False)
    isPublished = Column(Boolean)
