# qa_python
В этом проекте создан набор тестов для класса BooksCollector,проверяется функционал работы с коллецией книг,с жанрами и избранными книгами.

созданы тесты:

Инициализация класса:
        
    test_books_genre_type_dict -  проверка типов атрибутов
    test_favorites_type_list  -  проверка типов атрибутов
    test_books_genre_empty_dict -  проверка начальных значений
    test_favorites_type_list  -  проверка начальных значений
    test_genre_everyone  - проверка наличия всех жаноров
    test_genre_age_rating  - проверка наличия жанров ограниченных по возрасту

Добавление книг:
    test_add_new_book_len_40 - проверка корректного добавления с названием погр_знач 40 знаков
    test_add_new_book_invalid_len_41_fals - проверка ограничений по длине  41 знак

Работа с жанрами:
    test_set_book_genre_valid - установка корректного жанра
    test_set_book_genre_invalid_book - проверка несуществующей книги
    test_get_book_genre_valid - получение жанра

Фильтр по жанрам
    test_get_books_with_specific_genre_valid - выбор книг по жанру
    test_get_books_with_specific_genre_invalid - выбор по несуществующему жанру

Детские книги
    test_get_books_for_children_valid - проверка фильтрации детских книг
    test_get_books_for_children_all_restricted - проверка только запрещенных книг

Избранное
    test_add_book_in_favorites - добавление в избранное
    test_delete_book_from_favorites - удаление из избранного
    test_get_list_of_favorites_books - получение списка избранных

