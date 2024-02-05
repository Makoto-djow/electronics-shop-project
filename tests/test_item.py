import pytest
import csv
from src.item import Item

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
def csv_file():
    products_list = []
    with open('src/items.csv', 'r', encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products_list.append(row)
    return products_list


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


def test_instantiate_from_csv(csv_file):
    assert len(csv_file) == 5
    assert csv_file[1] == {'name': 'Ноутбук', 'price': '1000', 'quantity': '3'}
    assert csv_file[3]['price'] == '50'


def test_string_to_number(numbers):
    assert numbers == (10, 11, 12, 13)


def test_name(vacuum_cleaner_func):
    assert vacuum_cleaner_func.name == 'Пылесос'
    vacuum_cleaner_func.name = 'ПылесосПылесос'
    assert vacuum_cleaner_func.name == 'ПылесосПыл'
