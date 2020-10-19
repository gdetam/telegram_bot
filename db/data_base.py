"""this is data base's query creator."""

from config import connection_for_engine

from db.books import books

from sqlalchemy import Column, Table, asc, create_engine, func, select


class DB(object):
    """class with queries to DB."""

    LIMIT = 2

    @staticmethod
    def create_connector_db():
        """Initialize connection to the DB."""
        engine = create_engine(
            connection_for_engine,
            echo=True
        )
        connection = engine.connect()
        return connection

    @staticmethod
    def create_query_table(
            table_name: Table,
            current_page: int,
            column_name_for_order: Column):
        """Get a limit count of author or genre records from the DB."""
        offset = DB.LIMIT * current_page
        connection = DB.create_connector_db()
        r = table_name \
            .select() \
            .offset(offset) \
            .limit(DB.LIMIT) \
            .order_by(asc(column_name_for_order))
        result = connection.execute(r)
        DB.close_connector_db(connection)
        return result

    @staticmethod
    def get_books_by_item_id(
            item_id: int,
            current_page: int,
            column_name: Column):
        """Get a list of DB books matching id item."""
        offset = DB.LIMIT * current_page
        connection = DB.create_connector_db()
        r = select([books]) \
            .where(item_id == column_name) \
            .offset(offset) \
            .limit(DB.LIMIT) \
            .order_by(asc(books.c.name))
        result = connection.execute(r)
        DB.close_connector_db(connection)
        return result

    @staticmethod
    def get_book_by_id(
            book_id: int):
        """Get the selected books from DB."""
        connection = DB.create_connector_db()
        r = select([books]) \
            .where(book_id == books.c.id)
        result = connection.execute(r)
        DB.close_connector_db(connection)
        return result

    @staticmethod
    def get_count_page(
            table_name: Table):
        """Get from DB the count of pages containing authors or genres."""
        connection = DB.create_connector_db()
        c = select([func.count()]) \
            .select_from(table_name)
        result = connection.execute(c)
        count_page = round(int(result.fetchall()[0][0]) / DB.LIMIT) - 1
        DB.close_connector_db(connection)
        return count_page

    @staticmethod
    def get_count_books_pages_by_item_id(
            item_id: int,
            column_name: Column):
        """Get from DB the count of pages containing books."""
        connection = DB.create_connector_db()
        c = select([func.count()]) \
            .select_from(books) \
            .where(item_id == column_name)
        result = connection.execute(c)
        count_page = round(int(result.fetchall()[0][0]) / DB.LIMIT) - 1
        DB.close_connector_db(connection)
        return count_page

    @staticmethod
    def get_count_books():
        """Get the count of books from DB."""
        connection = DB.create_connector_db()
        c = select([func.count()]).select_from(books)
        result = connection.execute(c)
        count_books = int(result.fetchall()[0][0])
        DB.close_connector_db(connection)
        return count_books

    @staticmethod
    def close_connector_db(connection):
        """Close connection to DB."""
        connection.close()
