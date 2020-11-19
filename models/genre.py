"""this is genres table structure."""

from models.base import Base
from models.books_genres import books_genres

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Genres(Base):
    """This is Genres class for table structure."""

    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Books', secondary=books_genres)
