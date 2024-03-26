import uuid
from sqlalchemy import (
    UUID,
    Boolean,
    Column,
    DateTime,
    String,
    func,
    Integer,
    UniqueConstraint,
)
from ..database.core import Base


class Vendor(Base):
    """
    Represents a Square Vendor SQLAlchemy Model
    """

    __tablename__ = "vendors"

    id = Column(UUID, primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String(256), nullable=False, index=True)
    email = Column(String(256), nullable=False, index=True, unique=True)
    company_size = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)
    deleted = Column(Boolean, default=False)

    __table_args__ = (UniqueConstraint("email", name="unique_email"),)
