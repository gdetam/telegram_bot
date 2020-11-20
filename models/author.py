"""this is authors table structure."""

from models.base import Base

from sqlalchemy import Column, Integer, String


class Authors(Base):
    """This is Authors class for table structure."""

    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
