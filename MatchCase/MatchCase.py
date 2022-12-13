x = 1

match x:
  case 0:
    print('0')
  case 4:
    print('4')
  case 3: 
    print('3')
  case _ if x == 90:
    print(x)
  case _:
    print(x)