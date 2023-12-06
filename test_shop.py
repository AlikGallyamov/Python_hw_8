"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart(products={})


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000), f"Количество запрашиваемых товаров больше чем есть на складе"

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(50) == 950, f"На складе осталось неверное количество товаров"

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии

        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product, 15)
        cart.add_product(product, 5)
        assert cart.products[product] == 20, f"Количество товаров в корзине не равно ожидаемому"

    def test_remove_product(self, product, cart):
        cart.add_product(product, 30)
        cart.remove_product(product, 15)
        assert cart.products[product] == 15, f"Количество товаров в корзине не равно ожидаемому"

    def test_clear(self, cart, product):
        cart.add_product(product, 15)
        cart.clear()
        assert cart.products == {}
        f"Корзина не пустая"

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 15)
        assert cart.get_total_price() == 1500, f"Суммарная цена не равна ожидаемой"

    def test_buy(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()

    def test_buy(self, cart, product):
        cart.add_product(product, 20)
        cart.buy()
        assert cart.products == {}, f"Корзина не пустая, товар не был куплен"
