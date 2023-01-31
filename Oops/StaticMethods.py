class Math:
  def __init__(self, num):
    self.num = num

  @staticmethod
  def add(x, y):
    return x + y

m = Math(5)
print(m.num)
print(Math.add(5, 7))