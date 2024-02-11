from src.item import Item


class Phone(Item):
    """
    Дочерний класс для представления конкретного товара "Телефон"
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        """
        Создание экземпляра класса Phone

        :param name: Название товара. (Наследуется)
        :param price: Цена за единицу товара. (Наследуется)
        :param quantity: Количество товара в магазине. (Наследуется)
        :param number_of_sim: Количество сим-карт
        """

        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """
        Переопределяет repr и помимо имени класса и атрибутов родительского класса,
        также возвращает атрибут кол-ва сим-карт
        """

        return f'{self.__class__.__name__}(\'{self.name}\', {self.price}, {self.quantity}, {self.number_of_sim})'
