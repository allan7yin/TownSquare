from sqlalchemy import create_engine, UUID, Column, DateTime, Uuid, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import typing as t
from sqlalchemy.ext.declarative import as_declarative

from ..config import config

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class_registry: t.Dict = {}

@as_declarative(class_registry=class_registry)
class Base:
    """
    Abstract base class for all SqlAlchemy models
    """
    __abstract__ = True,
    id = Column(UUID(as_uuid=True), primary_key=True, default=Uuid.uuid4, index=True)
    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    def soft_delete(self):
        self.deleted_at = func.now()
