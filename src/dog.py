import datetime as dt
import json
from pathlib import Path
import uuid

from src.animal import Animal

class Dog(Animal):
  num_legs = 4

  def __init__(self, age, weight):
    if age < 0:
        raise ValueError('Age value must be greater than 0')
    if weight < 0:
        raise ValueError('Weight value must be greater than 0')
    super().__init__(age)
    self.weight = weight

  @staticmethod
  def bark(self):
    print('woof-woof')

  def is_puppy(self):
    if self.age <= 1:
      return True
    else:
      return False

  def eat(self):
    self.last_time_fed = datetime.datetime.now()
    self.weight = 1.01*self.weight

  def get_time_last_fed(self):
    time_sec_since_last_time_fed = (datetime.datetime.now() - self.last_time_fed).total_seconds()
    return time_sec_since_last_time_fed

  def is_hungry(self):
    if self.get_time_last_fed() > 10: # seconds
      return True
    else:
      return False

  # out_path is where the file will be written
  def save_to_json(self, out_path):
      unique_id = str(uuid.uuid4())
      # f_path is file path
      f_path = Path(out_path)/f'dog{unique_id}.json'
      json_data = {'age': self.age,
              'weight': self.weight}
      with open(f_path, 'w') as f:
          json.dump(json_data, f)
      return f_path

  @classmethod
  def load_from_json(cls, f_path):
      with open(f_path) as f:
          json_data = json.load(f)
      age = json_data['age']
      weight = json_data['weight']
      return cls(age, weight)

  def __repr__(self):
    return f'Dog(age={self.age}, weight={self.weight})'

  def __str__(self):
    return f"This is an dog that's {self.age} old"

  # equal (eq)
  def __eq__(self, other):
    return (self.age == other.age) and (self.weight == other.weight)

  # less than (lt)
  def __lt__(self, other):
    return self.weight < other.weight

# my_dog = Dog(3, 50)
# my_other_dog = Dog(3, 51)

# print('Is my dog equal to other dog in age and weight?', my_dog == my_other_dog)
# print('Is my dog heavier than other dog?', my_dog > my_other_dog)
# print('Is my dog a puppy?', my_dog.is_puppy())

# dog = Dog(age=5, weight=20)
# f_path = dog.save_to_json('/tmp')
# print(f_path)

dog = Dog.load_from_json(f_path='/tmp/dog90d98832-6fb7-4d24-aa3a-edf392063fd8.json')
print(dog)
print(dog.weight)
