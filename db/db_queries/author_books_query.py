"""this is author's books query in data base."""

from config import LIMIT

from db.db_queries.session_create import session

from models.book import Books


def get_author_books_by_item_id(
                                item_id: int,
                                current_page: int):
    """Get a list of DB author's books matching id item."""
    offset = LIMIT * current_page
    result: Books = session.query(Books) \
                           .filter(Books.author_id == item_id) \
                           .order_by(Books.name.asc()) \
                           .offset(offset) \
                           .limit(LIMIT) \
                           .all()
    return result
