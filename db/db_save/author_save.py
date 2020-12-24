"""Control authors from parser and save in data base."""


from db.db_queries.session_create import session

from models.author import Authors

from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound


def save_author(row: dict):
    """Author's control and save in data base."""
    try:
        result: Authors = session.query(Authors) \
                                 .filter(Authors.name == row.get('author_name')) \
                                 .one()
        return result

    except MultipleResultsFound:
        print('Такой автор уже есть в базе')

    except NoResultFound:
        result: Authors = Authors(name=row.get('author_name'))
        session.add(result)
        session.commit()
        return result
