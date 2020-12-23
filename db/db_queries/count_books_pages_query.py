"""this is count_books_pages query in data base."""

from config import LIMIT

from db.db_queries.session_create import session

from models.book import Books

from sqlalchemy import Column


def get_count_books_pages_by_item_id(
                                     item_id: int,
                                     column_name: Column):
    """Get from DB the count of pages containing books."""
    result: int = session.query(Books) \
                         .filter(item_id == column_name) \
                         .count()
    count_page = round(result / LIMIT) - 1
    return count_page
