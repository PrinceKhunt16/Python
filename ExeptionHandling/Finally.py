def func():
  try:
    nums = [1, 2, 3, 4]
    num = int(input('Enter the index '))
    print(nums[num])
    return 1
  except:
    print('Some error occured')
    return 0

  finally:
    print('I am always executed')

print(func())