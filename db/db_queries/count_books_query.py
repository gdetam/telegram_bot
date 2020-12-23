"""this is count_books query in data base."""

from db.db_queries.session_create import session

from models.book import Books


def get_count_books():
    """Get the count of books from DB."""
    result: int = session.query(Books) \
                         .count()
    count_books = int(result)
    return count_books
