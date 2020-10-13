from sqlalchemy import MetaData, Table, Column, Integer, String


meta = MetaData()

genres = Table(
    'genres', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)
