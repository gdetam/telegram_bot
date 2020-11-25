"""this is books_genres table structure."""

from models.base import Base

from sqlalchemy import Column, ForeignKey, Integer, Table

books_genres = Table('books_genres', Base.metadata,
                     Column('book_id', Integer, ForeignKey('books.id')),
                     Column('genre_id', Integer, ForeignKey('genres.id'))
                     )
