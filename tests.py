import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_too_long_name(self):
        collector = BooksCollector()
        long_name = 'x' * 41
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_set_book_genre_invalid_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Неизвестная книга', 'Фантастика')
        assert collector.get_book_genre('Неизвестная книга') is None

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Убийца')
        collector.set_book_genre('Убийца', 'Нон-фикшен')  # Неправильный жанр
        assert collector.get_book_genre('Убийца') is None

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')
        collector.add_new_book('Тайна третьей планеты')
        collector.set_book_genre('Тайна третьей планеты', 'Фантастика')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Дракула']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        collector.add_new_book('Ужас в квартире')
        collector.set_book_genre('Ужас в квартире', 'Ужасы')
        assert collector.get_books_for_children() == ['Детская книга']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Фаворит')
        collector.set_book_genre('Фаворит', 'Комедии')
        collector.add_book_in_favorites('Фаворит')
        assert 'Фаворит' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Убийца')
        collector.set_book_genre('Убийца', 'Детективы')
        collector.add_book_in_favorites('Убийца')
        collector.delete_book_from_favorites('Убийца')
        assert 'Убийца' not in collector.get_list_of_favorites_books()