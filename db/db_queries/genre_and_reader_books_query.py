"""this is genre's and reader's books query in data base."""

from config import LIMIT

from db.db_queries.session_create import session

from models import base
from models.book import Books


def get_genre_and_reader_books_by_item_id(table_name: base,
                                          item_id: int,
                                          current_page: int):
    """Get a list of DB genre's and reader's books matching id item."""
    offset = LIMIT * current_page
    result: Books = session.query(Books) \
                           .select_from(table_name) \
                           .join(table_name.books) \
                           .group_by(Books) \
                           .filter(table_name.id == item_id) \
                           .order_by(Books.name.asc()) \
                           .offset(offset) \
                           .limit(LIMIT) \
                           .all()
    return result
