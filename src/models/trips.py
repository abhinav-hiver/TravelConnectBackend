from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String
from sqlalchemy.sql.expression import func
from sqlalchemy.dialects.mysql import INTEGER
from src.models.users import Users
from .parent_model import ParentModel
from . import Base


class Trips(Base, ParentModel):

    __tablename__ = "trips"

    id = Column(BigInteger, primary_key=True)
    hosted_by = Column(BigInteger,  ForeignKey(Users.id), nullable=False)
    destination = Column(String(500))
    duration = Column(INTEGER)
    events = Column(String(500))
    status = Column(String(255))
    additional_info = Column(String(500))
    date_from = Column(DateTime)
    date_to = Column(DateTime)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())