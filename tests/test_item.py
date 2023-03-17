from src.item import Item
import pytest


@pytest.fixture
def test_object():
    return Item("Brick", 2.5, 100)


def test_item_calculate_total_price(test_object):
    assert test_object.calculate_total_price() == 250.0


def test_item_apply_discount(test_object):
    test_object.apply_discount()
    assert test_object.price == 2.5


def test_string_to_number():
    assert Item.string_to_number('111.234') == 111


def test_str_item(test_object):
    assert (str(test_object)) == "Brick"


def test_repr_item(test_object):
    assert (repr(test_object)) == "Item('Brick', 2.5, 100)"