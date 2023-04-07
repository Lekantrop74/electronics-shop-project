from src.keyboard import KeyBoard, Keyboard_language
import pytest


@pytest.fixture
def keyboard():
    return Keyboard_language()


def test_default_language(keyboard):
    assert keyboard.language == "EN"


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == "RU"


def test_change_lang_twice(keyboard):
    keyboard.change_lang().change_lang()
    assert keyboard.language == "EN"


def test_change_lang_invalid(keyboard):
    with pytest.raises(AttributeError):
        keyboard.language = "CH"


def test_keyboard_creation():
    keyboard = KeyBoard("Keyboard", 50.0, 10)
    assert keyboard.name == "Keyboard"
    assert keyboard.price == 50.0
    assert keyboard.quantity == 10

