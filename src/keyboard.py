from src.item import Item


class Keyboard_language:
    """
    Класс, описывающий язык клавиатуры.
    Атрибуты:
        __language (str): язык клавиатуры, задается при инициализации
    Методы:
        change_lang: меняет язык клавиатуры на противоположный
        language: свойство-геттер для доступа к текущему языку клавиатуры
    """

    def __init__(self, language: str = "EN"):
        """
        Конструктор класса Keyboard_language.
        Аргументы:
            language (str): язык клавиатуры, по умолчанию "EN"
        """
        self.__language = language

    def change_lang(self):
        """
        Меняет язык клавиатуры на противоположный.
        Возвращает:
            экземпляр класса Keyboard_language
        """
        if self.__language == "EN":
            self.__language = "RU"
            return self

        else:
            self.__language = "EN"
            return self

    @property
    def language(self) -> str:
        return self.__language


class KeyBoard(Item, Keyboard_language):
    """
    Класс, описывающий клавиатуру.
    Наследует классы:
        Item
        Keyboard_language
    Методы:
        __init__: конструктор класса
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Конструктор класса KeyBoard.
        Аргументы:
            name (str): название клавиатуры
            price (float): цена клавиатуры
            quantity (int): количество клавиатур
        """
        super().__init__(name, price, quantity)
        Keyboard_language.__init__(self)
