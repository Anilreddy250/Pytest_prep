# contents of test_append.py
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]


def test_int(order):
    # Act
    order.append(2)

    # Assert
    assert order == ["2" ,2 ]
# test_append.py

@pytest.fixture
def first_entry():  # <-- Change the 'm' to an 'n' here
    return []       # (or whatever your initial value is)

@pytest.fixture
def order(first_entry):
    return first_entry

def test_string(order):
    # your test code
    ...
@pytest.fixture
def order(first_entry):  # <-- Match the typo exactly
    return first_entry