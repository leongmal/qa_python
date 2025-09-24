from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_books_genre_type_dict(self):
        collector = BooksCollector()
        assert type(collector.books_genre) == dict

    def test_books_genre_empty_dict(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    def test_favorites_type_list(self):
        collector = BooksCollector()
        assert type(collector.favorites) == list

    def test_favorites_empty_list(self):
        collector = BooksCollector()
        assert collector.favorites == []

    @pytest.mark.parametrize('genre',['Фантастика', 'Ужасы', 'Детективы','Мультфильмы', 'Комедии'])
    def test_genre_true(self,genre):
        collector = BooksCollector()
        assert genre in collector.genre

    @pytest.mark.parametrize('range_age',['Ужасы', 'Детективы'])
    def test_genre_age_rating(self,range_age):
        collector = BooksCollector()
        assert range_age in collector.genre_age_rating

    def test_add_new_book_len_40(self):
        collector = BooksCollector()
        name = 'Это название очень длинное как 40 знаков'
        collector.add_new_book(name)
        assert collector.books_genre == {name:''}

    def test_add_new_book_len_41_fals(self):
        collector = BooksCollector()
        name = 'А это название очень длинное как 41 знак '
        collector.add_new_book(name)
        assert collector.books_genre != {name:''}

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Фантастика')
        assert collector.books_genre['Солярис'] == 'Фантастика'
    def test_set_book_genre_invalid_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Солярис', 'Фантастика')
        assert 'Фантастика' not in collector.books_genre

    def test_get_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Туманность Андромеды')
        collector.set_book_genre('Туманность Андромеды', 'Фантастика')
        assert collector.get_book_genre('Туманность Андромеды') == 'Фантастика'

    def test_get_books_with_specific_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Афоня')
        collector.set_book_genre('Афоня', 'Комедии')
        collector.add_new_book('Киндза-дза')
        collector.set_book_genre('Киндза-дза', 'Комедии')

        result = collector.get_books_with_specific_genre('Комедии')
        assert result == ['Афоня', 'Киндза-дза']

    def test_get_books_with_specific_genre_invalid(self):
        collector = BooksCollector()
        result = collector.get_books_with_specific_genre('Фэнтези')
        assert result == []

    def test_get_books_for_children_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка')
        collector.set_book_genre('Незнайка', 'Мультфильмы')
        collector.add_new_book('Буратино')
        collector.set_book_genre('Буратино', 'Комедии')
        collector.add_new_book('Челюсти')
        collector.set_book_genre('Челюсти', 'Ужасы')

        result = collector.get_books_for_children()
        assert result == ['Незнайка', 'Буратино']
        assert 'Челюсти' not in result

    def test_get_books_for_children_all_restricted(self):
        collector = BooksCollector()
        collector.add_new_book('Челюсти')
        collector.set_book_genre('Челюсти', 'Ужасы')
        collector.add_new_book('Игла')
        collector.set_book_genre('Игла', 'Детективы')

        result = collector.get_books_for_children()
        assert result == []
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        assert 'Война и мир' in collector.favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Бег')
        collector.add_book_in_favorites('Бег')
        collector.delete_book_from_favorites('Бег')
        assert 'Бег' not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Поединок')
        collector.add_book_in_favorites('Поединок')
        collector.add_new_book('Двойник')
        collector.add_book_in_favorites('Двойник')

        result = collector.get_list_of_favorites_books()
        assert result == ['Поединок', 'Двойник']

