"""Control reader's books from parser and save in data base."""

from db.db_queries.session_create import session

from models.book import Books
from models.reader import Readers


def save_books_readers(
                       book: Books,
                       reader: Readers):
    """Reader's books control and save in data base."""
    flag = False
    if book.readers is not None:
        for i in range(len(book.readers)):
            if book.readers[i].id is reader.id:
                flag = True
    if flag is False:
        book.readers.append(reader)
        session.add(book)
        session.commit()
