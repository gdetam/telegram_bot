"""this is book_by_id query in data base."""

from db.db_queries.session_create import session

from models.book import Books


def get_book_by_id(book_id: int):
    """Get the selected books from DB."""
    result: int = session.query(Books) \
                         .filter(book_id == Books.id)
    return result
