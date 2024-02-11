from src.item import Item


class LayoutMixing:
    """
    Класс для хранения и изменения раскладки клавиатуры.
    """

    def __init__(self, name, price, quantity, layout_1='EN', layout_2='RU'):
        """
        Создание экземпляра класса LayoutMixing

        :param name: Название товара. (Наследуется)
        :param price: Цена за единицу товара. (Наследуется)
        :param quantity: Количество товара в магазине. (Наследуется)
        :layout_1='EN': Первый язык раскладки
        :layout_2='RU': Второй язык раскладки
        """

        super().__init__(name, price, quantity)
        self.layout_1 = layout_1
        self.layout_2 = layout_2

    def changing_the_layout(self, layout):
        """
        Возвращает изменённую раскладку
        """

        if layout == self.layout_1:
            new_layout = self.layout_2
        else:
            new_layout = self.layout_1
        return new_layout


class Keyboard(LayoutMixing, Item):
    """
    Дочерний класс для представления конкретного товара "Телефон"
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса Keyboard

        :param name: Название товара. (Наследуется)
        :param price: Цена за единицу товара. (Наследуется)
        :param quantity: Количество товара в магазине. (Наследуется)
        :language: Язык раскладки
        """

        super().__init__(name, price, quantity)
        self.language = 'EN'

    def change_lang(self):
        """
        Изменяет язык раскладки на клавиатуре
        """

        self.language = super().changing_the_layout(self.language)
        return self.language
