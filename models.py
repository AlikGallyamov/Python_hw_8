from dataclasses import dataclass


@dataclass
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if not self.check_quantity(quantity):
            raise ValueError
        self.quantity = self.quantity - quantity
        return self.quantity

    def __hash__(self):
        return hash(self.name + self.description)


@dataclass
class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] = self.products[product] + buy_count
        else:
            self.products[product] = buy_count
        return self.products

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if remove_count is None or remove_count >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] = self.products[product] - remove_count
        return self.products

    def clear(self):

        self.products.clear()

    def get_total_price(self) -> float:
        total_price = [price.price * count for price, count in self.products.items()]
        return sum(total_price)

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for prod, quantity in self.products.copy().items():
            Product.buy(prod, quantity)
            if Product.check_quantity(prod, quantity) is True:
                del self.products[prod]
            else:
                raise ValueError
