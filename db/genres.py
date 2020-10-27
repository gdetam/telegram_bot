"""this is genres table structure."""

from sqlalchemy import Column, Integer, MetaData, String, Table


meta = MetaData()

genres = Table(
    'genres', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)
