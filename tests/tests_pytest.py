import pytest
from src.dog import Dog

@pytest.fixture()
def setup():
    dog = Dog(age=0.5, weight=10)
    yield dog

def test_is_puppy(setup):
    dog = setup
    assert dog.is_puppy() == True

def test_num_legs():
    assert Dog.num_legs == 4

def test_add_one_year(setup):
    dog = setup
    dog.add_one_year()
    assert dog.age == 1.5

def test_not_is_puppy(setup):
    dog = setup
    dog.add_one_year()
    assert dog.is_puppy() is False

def test_fail_invalid_age():
    with pytest.raises(ValueError):
        Dog(age=-1, weight=10)
