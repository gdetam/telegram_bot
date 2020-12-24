"""Control readers from parser and save in data base."""

from db.db_queries.session_create import session

from models.reader import Readers

from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound


def save_reader(row: dict):
    """Reader's control and save in data base."""
    try:
        result: Readers = session.query(Readers) \
                                 .filter(Readers.name == row.get('reader_name')) \
                                 .one()
        return result

    except MultipleResultsFound:
        print('Такой исполнитель уже есть в базе')

    except NoResultFound:
        result: Readers = Readers(name=row.get('reader_name'))
        session.add(result)
        session.commit()
        return result
