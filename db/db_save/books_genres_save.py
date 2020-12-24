"""Control genre's books from parser and save in data base."""

from db.db_queries.session_create import session

from models.book import Books
from models.genre import Genres


def save_books_genres(
                      book: Books,
                      genre: Genres):
    """Genre's books control and save in data base."""
    flag = False
    if book.genres is not None:
        for i in range(len(book.genres)):
            if book.genres[i].id is genre.id:
                flag = True
    if flag is False:
        book.genres.append(genre)
        session.add(book)
        session.commit()
