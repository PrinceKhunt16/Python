class Animal:
  name = ""

  def eat(self):
    print("I can Dance")

class Dog(Animal):
  def display(self):
    print(f"My name is {self.name}")

d = Dog()

d.name = "Jonny"
d.eat()

d.display()