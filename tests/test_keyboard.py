def test_keyboard_init(keyboard):
    assert keyboard.name == 'Клавиатура'
    assert keyboard.price == 4500
    assert keyboard.quantity == 42
    assert keyboard.pay_rate == 0.6
    assert keyboard.language == 'EN'


def test_keyboard__add__(phone, vacuum_cleaner_func, keyboard, table_class):
    table = table_class('Стол', 10000, 47)
    assert keyboard + keyboard == 84
    assert keyboard + vacuum_cleaner_func == 62
    assert keyboard + table is None
    assert table + table == 94
    assert keyboard + phone == 103


def test__keyboard__repr__(keyboard):
    assert repr(keyboard) == 'Keyboard(\'Клавиатура\', 4500, 42)'


def test_keyboard__str__(keyboard):
    assert str(keyboard.language) == "EN"
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"
    keyboard.change_lang()
    assert str(keyboard.language) == "EN"


def test_change_lang(keyboard):
    assert str(keyboard.language) == 'EN'
    keyboard.change_lang()
    assert str(keyboard.language) == 'RU'
