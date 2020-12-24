"""Control books from parser and save in data base."""

from db.db_queries.session_create import session

from models.author import Authors
from models.book import Books

from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound


def save_book(
              row: dict,
              author: Authors):
    """Book's control and save in data base."""
    try:
        result: Books = session.query(Books) \
                               .filter(Books.name == row.get('name')) \
                               .one()
        return result

    except MultipleResultsFound:
        print('Такая книга уже есть в базе')

    except NoResultFound:
        result: Books = Books(name=row.get('name'),
                              description=row.get('description'),
                              book_url=row.get('book_url'),
                              author=author)
        session.add(result)
        session.commit()
        return result
