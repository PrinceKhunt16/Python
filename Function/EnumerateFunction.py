marks = [12, 34, 89, 23, 45]

for index, mark in enumerate(marks):
  print(index, mark)

for index, mark in enumerate(marks, start = 1):
  print(index, mark)