"""Control genres from parser and save in data base."""

from db.db_queries.session_create import session

from models.genre import Genres

from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound


def save_genre(row: dict):
    """Genre's control and save in data base."""
    try:
        result: Genres = session.query(Genres) \
                                .filter(Genres.name == row.get('genre_name')) \
                                .one()
        return result

    except MultipleResultsFound:
        print('Такой жанр уже есть в базе')

    except NoResultFound:
        result: Genres = Genres(name=row.get('genre_name'))
        session.add(result)
        session.commit()
        return result
