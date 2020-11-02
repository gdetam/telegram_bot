"""this is readers table structure."""

from sqlalchemy import Column, Integer, MetaData, String, Table


meta = MetaData()

readers = Table(
    'readers', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)
