"""this is readers table structure."""

from models.base import Base
from models.books_readers import books_readers

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Readers(Base):
    """This is Readers class for table structure."""

    __tablename__ = 'readers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Books', secondary=books_readers)
