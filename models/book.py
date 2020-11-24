"""this is books table structure."""

from models.base import Base
from models.books_genres import books_genres
from models.books_readers import books_readers

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Books(Base):
    """This is Books class for table structure."""

    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    book_url = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Authors', foreign_keys=[author_id])
    genres = relationship('Genres', secondary=books_genres, lazy=False)
    readers = relationship('Readers', secondary=books_readers, lazy=False)
