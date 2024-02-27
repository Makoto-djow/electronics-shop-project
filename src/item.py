import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = 'Повреждение файла.'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """

        import os
        head, tail = os.path.split(file)
        try:
            with open(os.path.join('..', head, tail), newline='', encoding='cp1251') as csvfile:
                cls.all.clear()
                reader = csv.DictReader(csvfile)
                for rov in reader:
                    name = str(rov['name'])
                    price = float(rov['price'])
                    quantity = int(rov['quantity'])
                    cls(name, price, quantity)
                if len(cls.all) != 5:
                    raise InstantiateCSVError('Файл items.csv поврежден')

        except FileNotFoundError:
            print('Отсутствует файл items.csv')
            raise

    @staticmethod
    def string_to_number(numbers_string):
        """
        Статический метод, возвращающий число из числа-строки
        """

        numbers_int = int(float(numbers_string))
        return numbers_int

    @property
    def name(self):
        """
        Геттер возвращающий name
        """

        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Сеттер, который проверяет new_name на кол-во символов (небольше 10)
        """

        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    def __repr__(self):
        """
        Возвращает имя класса и атрибуты его экземпляра
        """

        return f'{self.__class__.__name__}(\'{self.__name}\', {self.price}, {self.quantity})'

    def __str__(self):
        """
        Возвращает имя класса
        """

        return self.__name

    def __add__(self, other):
        """
        Позволяет складывать экземпляры класса Item между собой по количеству товара в магазине
        """

        if isinstance(other, Item):
            return int(self.quantity) + int(other.quantity)
        else:
            return None
