from sqlalchemy import MetaData, Table, Column, Integer, String


meta = MetaData()

authors = Table(
    'authors', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String)
)
