from functools import reduce

nums = [1, 9, 4, 6, 4]

# print(nums)
# nums.append(8)
# print(nums)

# nums.sort()
# print(nums)
# nums.reverse()
# print(nums)

# print(nums.index(4))

# print(nums.count(4))

# numms = nums
# numms[0] = 0
# print(nums)

# numms = nums.copy()
# numms[0] = 0
# print(nums)
# print(numms)

# nums.insert(1, 7)
# print(nums)

# numms = [89, 23, 43]
# nums.extend(numms)
# print(nums)

# numms = [89, 23, 43]
# nummms = nums + numms
# print(nums)
# print(numms)
# print(nummms)

def cube(x):
  return x * x * x

nums = [1, 2, 3, 4, 5]

# cubes = []
# for item in nums:
#   cubes.append(cube(item))
# print(cubes)

# cubes = list(map(cube, nums))
# print(cubes)

# cubes = list(map(lambda x: x * x * x, nums))
# print(cubes)

# def even(x):
#   return x % 2 == 0

# evens = list(filter(even, nums))
# print(evens)

# cubes = list(filter(lambda x: x % 2 == 0, nums))
# print(cubes)

# def sum(x, y):
#   return x + y

# sum = reduce(sum, nums)
# print(sum)

# sum = reduce(lambda x, y: x + y, nums)
# print(sum)