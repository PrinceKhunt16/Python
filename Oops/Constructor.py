class Person:
  def __init__(self, name, occupation):
    self.name = name
    self.occupation = occupation

  def info(self):
    print(f"{self.name} is a {self.occupation}")

p = Person('John', 'Developer')
b = Person('Ram', 'HR')

p.info()
b.info()