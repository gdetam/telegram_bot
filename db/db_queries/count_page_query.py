"""this is count_page query in data base."""

from config import LIMIT

from db.db_queries.session_create import session

from models import base


def get_count_page(table_name: base):
    """Get from DB the count of pages containing authors or genres or readers."""
    result: int = session.query(table_name) \
                         .count()
    count_page = round(result / LIMIT) - 1
    return count_page
