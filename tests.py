import pytest

from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Pride and Prejudice and Zombies')
        collector.add_new_book('What to do if your cat wants to kill you')
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_for_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Pride and Prejudice and Zombies')
        collector.set_book_genre('Pride and Prejudice and Zombies', 'Horrors')
        assert collector.get_book_genre('Pride and Prejudice and Zombies') == 'Horrors'

    def test_get_books_for_children_one_book(self, books_set):
        collector = BooksCollector()
        collector.books_genre = books_set
        assert list(collector.get_books_for_children()) == ['The Hitchhiker’s Guide to the Galaxy']

    def test_add_new_book_in_favorites_one_book(self, books_set):
        collector = BooksCollector()
        collector.books_genre = books_set
        collector.add_book_in_favorites('Pride and Prejudice and Zombies')
        assert list(collector.get_list_of_favorites_books()) == ['Pride and Prejudice and Zombies']

    def test_delete_book_from_favorites_one_book(self, books_set):
        collector = BooksCollector()
        collector.books_genre = books_set
        collector.add_book_in_favorites('Pride and Prejudice and Zombies')
        collector.delete_book_from_favorites('Pride and Prejudice and Zombies')
        assert list(collector.get_list_of_favorites_books()) == []

    @pytest.mark.parametrize('name', ['The Life, Extraordinary and Amazing Adventures of Robinson Crusoe', ''])
    def test_add_new_book_incorrect_names(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_get_books_with_specific_genre_one_book(self, books_set):
        collector = BooksCollector()
        collector.books_genre = books_set
        assert collector.get_books_with_specific_genre('Sci-Fi') == ['The Hitchhiker’s Guide to the Galaxy']

    @pytest.mark.parametrize('name, genre', [
        ['Les trois mousquetaires', 'Adventures'],
        ['Anathem', 'Sci-Fi'],
        ['Anathem', '']])
    def test_set_book_genre_incorrect_book_and_genre(self, name, genre, books_set):
        collector = BooksCollector()
        collector.books_genre = books_set
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) is None

    @pytest.mark.parametrize('name, genre', [
        ['Les trois mousquetaires', 'Adventures'],
        ['Anathem', 'Sci-Fi'],
        ['Anathem', '']])
    def test_get_books_for_children_incorrect_genres(self, name, genre):
        collector = BooksCollector()
        assert collector.get_books_for_children() == []


