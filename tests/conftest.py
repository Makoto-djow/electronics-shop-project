import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard


@pytest.fixture
def vacuum_cleaner_func():
    vacuum_cleaner = Item('Пылесос', 25999.99, 20)
    Item.pay_rate = 0.7
    return vacuum_cleaner


@pytest.fixture
def laptop_func():
    laptop_func = Item('Ноутбук', 15000, 34)
    laptop_func.pay_rate = 0.4
    return laptop_func


@pytest.fixture
def phone():
    phone_func = Phone('Телефон', 12000, 61, 2)
    phone_func.pay_rate = 0.2
    return phone_func


@pytest.fixture()
def table_class():
    class Table:
        def __init__(self, name: str, price: float, quantity: int) -> None:
            self.__name = name
            self.price = price
            self.quantity = quantity

        def __add__(self, other):
            return self.quantity + other.quantity
    return Table


@pytest.fixture
def keyboard():
    keyboard_func = Keyboard('Клавиатура', 4500, 42)
    Item.pay_rate = 0.6
    return keyboard_func


@pytest.fixture
def numbers():
    number1 = Item.string_to_number('10')
    number2 = Item.string_to_number('11.0')
    number3 = Item.string_to_number('12.14')
    number4 = Item.string_to_number('13.7')
    return number1, number2, number3, number4
