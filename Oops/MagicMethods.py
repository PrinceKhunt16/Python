class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"I'm {self.name}."
    
p = Person("Princeter")
print(p.__str__())