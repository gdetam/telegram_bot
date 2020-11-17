"""this is genres table structure."""

from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

from models.base import Base
from models.books_genres import books_genres


class Genres(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Books", secondary=books_genres)
