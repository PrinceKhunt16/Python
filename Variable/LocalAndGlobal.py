x = 4 
print(x)

def func():
  global x
  x = 5
  y = 7 

  print(x)
  print(y)

func()
print(x)