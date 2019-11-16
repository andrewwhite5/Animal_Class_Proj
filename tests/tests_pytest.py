import pytest
import glob
import os
import json

from src.dog import Dog


@pytest.fixture()
def setup():
    dog = Dog(age=0.5, weight=10)
    f_path = dog.save_to_json(out_path='/tmp')
    yield dog, f_path
    [os.remove(f_path) for f_path in glob.glob('/tmp/dog_*.json')]


def test_is_puppy(setup):
    dog, _ = setup
    assert dog.is_puppy() == True


def test_num_legs():
    assert Dog.num_legs == 4


def test_add_one_year(setup):
    dog, _ = setup
    dog.add_one_year()
    assert dog.age == 1.5


def test_not_is_puppy(setup):
    dog, _ = setup
    dog.add_one_year()
    assert dog.is_puppy() is False


def test_fail_invalid_age():
    with pytest.raises(ValueError):
        Dog(age=-1, weight=10)


def test_save_to_json(setup):
    dog, f_path = setup
    with open(f_path) as f:
        json_data = json.load(f)
    assert json_data['age'] == 0.5
    assert json_data['weight'] == 10


def test_load_from_json(setup):
    dog, _ = setup
    f_list = glob.glob('/tmp/*.json')
    assert len(f_list) == 1
    dog = Dog.load_from_json(f_list[0])
