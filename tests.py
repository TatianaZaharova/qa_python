from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # приме теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books (self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_similar_books(self): # добавление двух одинаковых книг
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1

    def test_add_rating_to_absent_book_fails(self): #Добавить рейтинг в несуществующую книгу
        collector = BooksCollector()
        collector.set_book_rating('33 нигретенка', 5)
        assert collector.books_rating.get('34 нигретенка') is None

    def test_cant_set_rating_less_than_one(self): # не может быть рейтинга меньше 1
        collector = BooksCollector()
        collector.add_new_book('33 нигретенка')
        collector.set_book_rating('33 нигретенка', 0)
        assert collector.favorites == []
        assert collector.books_rating == {'33 нигретенка': 1}

    def test_cant_set_rating_greater_than_ten(self): # не может быть рейтинга больше 10
        collector = BooksCollector()
        collector.add_new_book('33 нигретенка')
        collector.set_book_rating('33 нигретенка', 11)
        assert collector.favorites == []
        assert collector.books_rating == {'33 нигретенка': 1}

    def test_absent_book_has_no_rating(self): # у не добавленной книги нет рейтинга.
        collector = BooksCollector()
        collector.add_new_book('33 нигретенка')
        rating = collector.get_book_rating('34 нигретенка')
        assert   rating is None

    def test_get_books_with_specific_rating(self): # Получить книги с определенным рейтингом
        collector = BooksCollector()
        collector.add_new_book('33 нигретенка')
        collector.add_new_book('34 нигретенка')
        collector.add_new_book('99 проблем')
        collector.set_book_rating('34 нигретенка', 7)
        result = collector.get_books_with_specific_rating(1)
        assert ['33 нигретенка', '99 проблем'] == result


    def test_add_book_to_favorites(self): # Добавление книги в избранное
        collector = BooksCollector()
        collector.add_new_book('33 нигретенка')
        collector.add_book_in_favorites('33 нигретенка')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books(self): # Полусить лист избраных книг
        collector = BooksCollector()
        collector.add_new_book('33 нигретенка')
        collector.add_book_in_favorites('33 нигретенка')
        assert collector.get_list_of_favorites_books() == ['33 нигретенка']


    def test_delete_from_favorites(self): # Удалить из списка избранных книг
        collector = BooksCollector()
        collector.add_new_book('33 нигретенка')
        collector.add_book_in_favorites('33 нигретенка')
        collector.delete_book_from_favorites('33 нигретенка')
        assert len(collector.get_list_of_favorites_books()) == 0