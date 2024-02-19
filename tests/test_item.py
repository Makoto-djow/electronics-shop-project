from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


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


def test_item__add__(laptop_func, table_class, phone):
    table = table_class('Стол', 10000, 47)
    assert laptop_func + table is None
    assert laptop_func + phone == 95
