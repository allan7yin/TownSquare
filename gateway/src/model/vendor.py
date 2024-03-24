from sqlalchemy import Column, Integer, String
from ..database.core import Base

class Vendor(Base):
    """
    Represents a Square Vendor SQLAlchemy Model
    """
    __tablename__ = "vendors"
    name = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)
    company_size = Column(Integer, nullable=False)
