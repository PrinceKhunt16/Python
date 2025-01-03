class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
p1 = Point(10, 10)
p2 = Point(20, 20)
p3 = p1 + p2

print(p3.x, p3.y)