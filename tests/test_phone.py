from src.phone import Phone
import pytest


@pytest.fixture
def test_object():
    return Phone("Heavy_Brick", 2.5, 100, 2)


def test_number_of_sim_setter_valid_value(test_object):
    test_object.number_of_sim = 2
    assert test_object.number_of_sim == 2


def test_number_of_sim_setter_zero_value(test_object):
    with pytest.raises(ValueError):
        test_object.number_of_sim = 0


def test_number_of_sim_setter_negative_value(test_object):
    with pytest.raises(ValueError):
        test_object.number_of_sim = -1

def test_repr_method(test_object):
    test_object = Phone("iPhone", 999, 10, 2)
    assert repr(test_object) == "Phone('iPhone', 999, 10, 2)"
