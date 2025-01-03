class Animal:
    def make_sound(self):
        return "Animal is making sound."
    
class Dog(Animal):
    def make_sound(self):
        return "Dog is making sound."
    
class Cat(Animal):
    def make_sound(self):
        return super().make_sound()
    
dog = Dog()
cat = Cat()

print(dog.make_sound())
print(cat.make_sound())