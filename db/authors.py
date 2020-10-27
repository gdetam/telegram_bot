"""this is authors table structure."""

from sqlalchemy import Column, Integer, MetaData, String, Table


meta = MetaData()

authors = Table(
    'authors', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String)
)
