def test_phone_init(phone):
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


def test__phone__repr__(phone):
    assert repr(phone) == 'Phone(\'Телефон\', 12000, 61, 2)'
