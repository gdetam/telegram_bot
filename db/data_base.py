from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


engine = create_engine('postgres://postgres:fallen365@127.0.0.1:5432/telegram_bot_audiobooks', echo=True)
connection = engine.connect()
meta = MetaData()

authors = Table(
    'authors', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String)
)

genres = Table(
    'genres', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)


def create_query_db(engine, table_name: Table):
    connection = engine.connect()
    r = table_name.select().offset(0).limit(2)
    result = connection.execute(r)
    for row in result:
       print(row)


create_query_db(engine, authors)
connection.close()


# ////////////

'''
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
'''

'''
offset = 0
limit = 2

connection = engine.connect()
t = text("SELECT * FROM authors ORDER BY last_name ASC  LIMIT " + str(limit) + " OFFSET " + str(offset))
result = connection.execute(t)
for row in result:
    print(row)

connection.close()

# t = query(Author).filter(autors).limit(2).all()
'''
'''
page = 0
page_size = 2


def q(filter, page: int, page_size: int):
    query = session.query(Author).filter(filter).all()
    if page_size:
        query = query.limit(page_size)
    if page:
        query = query.offset(page * page_size)
    return query


print(q(Author.author_id == 1, page, page_size))
'''
