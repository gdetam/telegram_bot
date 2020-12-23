"""this is create session for connect data base."""

from config import CONNECTION_FOR_ENGINE

from models import base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(CONNECTION_FOR_ENGINE)

base.Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)

session: Session = Session()
