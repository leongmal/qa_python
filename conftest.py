import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()
@pytest.fixture
def add_book_new(collector):
    def _add_book(name, ganre=None):
        collector.add_new_book(name)
        collector.set_book_genre(name,ganre)
    return _add_book