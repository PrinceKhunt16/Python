# class Employee:
#   def __init__(self):
#     self.name = 'John'

# e = Employee()
# print(e.name)


# Private Access Modifiers

# class Employee:
#   def __init__(self):
#     self.__name = 'John'

# e = Employee()
# print(e._Employee__name)

# print(e.__dir__())


# Protected Access Modifiers

class Student:
  def __init__(self):
    self._name = 'John'

  def _funName(self):
    return 'Hyy I am John'

class Subject(Student):
  pass

stu = Student()
sub = Subject()

print(dir(stu))

print(stu._name)
print(sub._funName())

print(stu._name)
print(sub._funName())