"""this is table query in data base."""

from config import LIMIT

from db.db_queries.session_create import session

from models import base

from sqlalchemy import Column


def create_query_table(
        table_name: base,
        current_page: int,
        column_name_for_order: Column):
    """Get a limit count of author or genre or reader records from the DB."""
    offset = LIMIT * current_page
    result: table_name = session \
        .query(table_name) \
        .order_by(column_name_for_order.asc()) \
        .offset(offset) \
        .limit(LIMIT) \
        .all()
    return result
