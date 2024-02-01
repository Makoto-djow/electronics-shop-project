import pytest
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
    assert laptop_func.price == 10500
