class Animal:
  def __init__(self, age):
    self.age = age

  def __repr__(self):
    return f'Animal(age={self.age})'

  def __str__(self):
    return f'This is an animal that is {self.age} years old.'

  def age_next_year(self):
    return self.age + 1

  def add_one_year(self):
    self.age = self.age + 1
