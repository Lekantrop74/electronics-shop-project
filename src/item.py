from src.utils import load_csv_list
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item
        :param name: Название товара
        :param price: Цена за единицу товара
        :param quantity: Количество товара в магазине
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name) > 10:
            raise Exception("Длина наименования товара превышает 10 символов.")
        self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине
        :return: Общая стоимость товара
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара"""
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """Cоздаём экзепляры класса на основе данных их файла"""
        cls.all = []
        for data in load_csv_list():
            cls(*data)

    @staticmethod
    def string_to_number(number: str) -> int:
        """Cтатический метод, возвращающий число из числа-строки
        :return: Число в нужном нам формате
        """
        return int(number.split(".")[0])

    def __str__(self):
        """Тандер для вывода информации об экземпляре"""
        return f"{self.__name}"

    def __repr__(self):
        """Тандер для вывода информации об экземпляре"""
        return f"{self.__class__.__name__}{self.__name, self.price, self.quantity}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Складывать можно только объекты Item и дочерние от них.")
        else:
            return self.quantity + other.quantity
