import pytest

@pytest.fixture
def first_entry():
    return "a"
@pytest.fixture
def order(first_entry):
    return [first_entry]
def test_string(order):
    order.append("b")
    assert order == ["a", "b"]

def first_entry():
    return "a"


def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]


entry = first_entry()
the_list = order(first_entry=entry)
test_string(order=the_list)



import pytest

@pytest.fixture
def first_entry():
    return "a"

@pytest.fixture
def order(first_entry):
    return [first_entry]

def test_string(order):
    order.append("b")
    assert order == ["a","b"]

def test_int(order):
    order.append(2)
    assert order == ["a", 2]


# class MailAdminClient:
#     def create_user(self):
#         return MailUser()
    