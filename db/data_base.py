"""this is data base's query creator."""
from sqlalchemy.orm import sessionmaker

from config import CONNECTION_FOR_ENGINE
from models import base

from models.book import Books

from sqlalchemy import Column, create_engine


class DB(object):
    """class with queries to DB."""
    engine = create_engine(CONNECTION_FOR_ENGINE)

    base.Base.metadata.create_all(engine, checkfirst=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    LIMIT = 2

    @staticmethod
    def create_connector_db():
        """Initialize connection to the DB."""
        engine = create_engine(
            CONNECTION_FOR_ENGINE,
            echo=True
        )
        connection = engine.connect()
        return connection

    @staticmethod
    def create_query_table(table_name: base,
                           current_page: int,
                           column_name_for_order: Column):
        """Get a limit count of author or genre records from the DB."""
        offset = DB.LIMIT * current_page
        result: table_name = DB.session \
                               .query(table_name) \
                               .order_by(column_name_for_order.asc()) \
                               .offset(offset) \
                               .limit(DB.LIMIT).all()
        return result

    @staticmethod
    def get_books_by_item_id(
            item_id: int,
            current_page: int,
            column_name: Column):
        """Get a list of DB books matching id item."""
        offset = DB.LIMIT * current_page
        result: Books = DB.session \
            .query(Books) \
            .filter(item_id == column_name) \
            .order_by(Books.name.asc()) \
            .offset(offset) \
            .limit(DB.LIMIT).all()
        return result

    @staticmethod
    def get_book_by_id(
            book_id: int):
        """Get the selected books from DB."""
        result: int = DB.session.query(Books).filter(book_id == Books.id)
        return result

    @staticmethod
    def get_count_page(table_name: base):
        """Get from DB the count of pages containing authors or genres."""
        result: int = DB.session.query(table_name).count()
        count_page = round(result / DB.LIMIT) - 1
        return count_page

    @staticmethod
    def get_count_books_pages_by_item_id(
            item_id: int,
            column_name: Column):
        """Get from DB the count of pages containing books."""
        result: int = DB.session.query(Books).filter(item_id == column_name).count()
        count_page = round(result / DB.LIMIT) - 1
        return count_page

    @staticmethod
    def get_count_books():
        """Get the count of books from DB."""
        result: int = DB.session.query(Books).count()
        count_books = int(result)
        return count_books

    @staticmethod
    def close_connector_db(connection):
        """Close connection to DB."""
        connection.close()
