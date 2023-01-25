def greet(fx):
  def mfx(*args, **kwargs):
    print('Good Morning')
    fx(*args, **kwargs)
    print('Thanks You')
  return mfx

@greet
def sayHyy():
  print('sayHyy')

sayHyy()

def howAreYou():
  print('How Are You')

greet(howAreYou)()

def add(x, y):
  print(x + y)

greet(add)(1, 2)