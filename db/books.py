"""this is books table structure."""

from sqlalchemy import Column, Integer, MetaData, String, Table


meta = MetaData()

books = Table(
    'books', meta,
    Column('id', Integer, primary_key=True),
    Column('author_id', Integer),
    Column('genre_id', Integer),
    Column('name', String),
    Column('url', String)
)