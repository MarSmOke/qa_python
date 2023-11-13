import pytest

from main import BooksCollector


@pytest.fixture #фикстура, которая создаёт словарь с книгами и жанрами
def books_set():
    books_set = BooksCollector()
    books_set.add_new_book('Pride and Prejudice and Zombies')
    books_set.add_new_book('The Hitchhiker’s Guide to the Galaxy')
    books_set.set_book_genre('Pride and Prejudice and Zombies', 'Horrors')
    books_set.set_book_genre('The Hitchhiker’s Guide to the Galaxy', 'Sci-Fi')
    return books_set.books_genre
