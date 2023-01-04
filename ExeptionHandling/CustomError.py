num = int(input('Enter any value between 5 and 9 '))

if(num < 5 or num > 9):
  raise ValueError('Num should be between 5 and 9')