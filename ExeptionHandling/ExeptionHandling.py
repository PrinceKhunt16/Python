# num = input('Enter any number ')

# try:
#   for i in range(1, 11):
#     print(f'{int(i)} X {num} = {int(num) * i}')
# except Exception as e:
#   print('Invalid input')

try: 
  num = int(input('Enter any index '))
  nums = [6, 3]
  print(nums[num])
except ValueError:
  print('Number entered is not an index')
except IndexError:
  print('Index Error')