"""this is file save content from parser in data base."""

import json

from config import PATH, inserter_flag

from db.db_save.author_save import save_author
from db.db_save.book_save import save_book
from db.db_save.books_genres_save import save_books_genres
from db.db_save.books_readers_save import save_books_readers
from db.db_save.genre_save import save_genre
from db.db_save.reader_save import save_reader


def books_handler(inserter_flag: bool):
    """Read the books.json file and inserts in data base."""
    if inserter_flag:
        with open(PATH, 'r', newline='', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for row in data:
                author = save_author(row)
                book = save_book(row, author)
                reader = save_reader(row)
                genre = save_genre(row)
                save_books_genres(book, genre)
                save_books_readers(book, reader)


books_handler(inserter_flag)
