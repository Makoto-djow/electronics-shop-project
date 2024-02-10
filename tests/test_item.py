import pytest
from src.item import Item
from src.phone import Phone

"""Здесь надо написать тесты с использованием pytest для модуля item."""


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
def numbers():
    number1 = Item.string_to_number('10')
    number2 = Item.string_to_number('11.0')
    number3 = Item.string_to_number('12.14')
    number4 = Item.string_to_number('13.7')
    return number1, number2, number3, number4


def test_item_init(vacuum_cleaner_func, laptop_func):
    assert vacuum_cleaner_func.name == 'Пылесос'
    assert vacuum_cleaner_func.price == 25999.99
    assert vacuum_cleaner_func.quantity == 20
    assert vacuum_cleaner_func.pay_rate == 0.7
    assert Item.all == [vacuum_cleaner_func, laptop_func]


def test_calculate_total_price(vacuum_cleaner_func, laptop_func):
    assert vacuum_cleaner_func.calculate_total_price() == 519999.80000000005
    assert laptop_func.calculate_total_price() == 510000


def test_apply_discount(vacuum_cleaner_func, laptop_func):
    vacuum_cleaner_func.apply_discount()
    laptop_func.apply_discount()
    assert vacuum_cleaner_func.price == 18199.993
    assert laptop_func.price == 6000


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5


def test_string_to_number(numbers):
    assert numbers == (10, 11, 12, 13)


def test_name(vacuum_cleaner_func, laptop_func):
    assert vacuum_cleaner_func.name == 'Пылесос'
    vacuum_cleaner_func.name = 'ПылесосПылесос'
    assert vacuum_cleaner_func.name == 'ПылесосПыл'
    assert laptop_func.name == 'Ноутбук'
    laptop_func.name = 'Ноут'
    assert laptop_func.name == 'Ноут'


def test__repr__(vacuum_cleaner_func):
    assert repr(vacuum_cleaner_func) == 'Item(\'Пылесос\', 25999.99, 20)'


def test__str__(laptop_func):
    assert str(laptop_func) == 'Ноутбук'


def test_phone_init(phone, vacuum_cleaner_func):
    assert phone.name == 'Телефон'
    assert phone.price == 12000
    assert phone.quantity == 61
    assert phone.pay_rate == 0.2


def test_phone__add__(phone, vacuum_cleaner_func, laptop_func, table_class):
    table = table_class('Стол', 10000, 47)
    assert phone + laptop_func == 95
    assert phone + vacuum_cleaner_func == 81
    assert phone + table is None
    assert table + table == 94
    assert phone + phone == 122


def test_item__add__(laptop_func, table_class, phone):
    table = table_class('Стол', 10000, 47)
    assert laptop_func + table is None
    assert laptop_func + phone == 95


def test__phone__repr__(phone):
    assert repr(phone) == 'Phone(\'Телефон\', 12000, 61, 2)'
