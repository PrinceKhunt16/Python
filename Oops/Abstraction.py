from abc import ABC, abstractmethod

# https://medium.com/data-bistrot/abstraction-in-python-oop-c4da042f9eaf

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "The car moves on the road"

class Boat(Vehicle):
    def move(self):
        return "The boat sails on the water"

# Usage
car = Car()
print(car.move())  # Output: The car moves on the road

boat = Boat()
print(boat.move())  # Output: The boat sails on the water