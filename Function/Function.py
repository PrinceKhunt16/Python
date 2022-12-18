### Example 1

# def sumOfTwoNumber(a, b):
#   mean = int(a) + int(b)
#   return mean

# a = input('Enter value of a ')
# b = input('Enter value of b ')

# sum = sumOfTwoNumber(a, b)
# print('Sum of a and b is', sum)

### Example 2

# def concatName(name, surename):
#   return name + ' ' + surename

# name = 'John'
# surename = 'Doe'

# fullName = concatName(name, surename)
# print('Your full name is', fullName)

### Example 3

# def average(a = 0, b = 0):
#   print('The average is', (a + b) / 2)

# average()

### Example 4

# def average(a, b):
#   print('The average is', (a + b) / 2)

# average(10, 20)

### Example 5

# def average(a, b):
#   print('The average is', (a + b) / 2)

# average(b = 20, a = 10)

### Example 6

# def average(*nums):
#   num = 0
#   for n in nums:
#     num += n
#   return num / len(nums)

# c = average(1, 2, 3, 4, 5)
# print(c)

### Example 7

# def name(**name):
#   print('Hello,', name['fname'], name['mname'], name['lname'])

# name(mname = 'Buchanan', lname = 'Barnes', fname = 'James')