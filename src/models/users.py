from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String
from sqlalchemy.sql.expression import func
from sqlalchemy.dialects.mysql import INTEGER
from .parent_model import ParentModel
from . import Base


class Users(Base, ParentModel):

    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255))
    contact_no = Column(String(15))
    age = Column(INTEGER)
    email_id = Column(String(500))
    interests = Column(String(500))
    profile_photo = Column(String(500))
    places_visited = Column(String(500))
    other_info = Column(String(500))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
