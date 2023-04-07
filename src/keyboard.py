from src.item import Item


class Keyboard_language:
    """
    �����, ����������� ���� ����������.
    ��������:
        __language (str): ���� ����������, �������� ��� �������������
    ������:
        change_lang: ������ ���� ���������� �� ���������������
        language: ��������-������ ��� ������� � �������� ����� ����������
    """

    def __init__(self, language: str = "EN"):
        """
        ����������� ������ Keyboard_language.
        ���������:
            language (str): ���� ����������, �� ��������� "EN"
        """
        self.__language = language

    def change_lang(self):
        """
        ������ ���� ���������� �� ���������������.
        ����������:
            ��������� ������ Keyboard_language
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
    �����, ����������� ����������.
    ��������� ������:
        Item
        Keyboard_language
    ������:
        __init__: ����������� ������
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        ����������� ������ KeyBoard.
        ���������:
            name (str): �������� ����������
            price (float): ���� ����������
            quantity (int): ���������� ���������
        """
        super().__init__(name, price, quantity)
        Keyboard_language.__init__(self)
