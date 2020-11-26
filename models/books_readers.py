"""this is books_readers table structure."""

from models.base import Base

from sqlalchemy import Column, ForeignKey, Integer, Table


books_readers = Table('books_readers', Base.metadata,
                      Column('book_id', Integer, ForeignKey('books.id')),
                      Column('reader_id', Integer, ForeignKey('readers.id'))
                      )
