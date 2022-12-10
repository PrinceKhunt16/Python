# String are immutable and it's function doesn't change it but gives a new one instead.

name = 'John! Don!'

print(len(name))
print(name.upper())
print(name.lower())
print(name.rstrip('!'))
print(name.rstrip('!').replace('John', 'John Doe'))
print(name.split(' '))
print(name.split(' ')[0].capitalize())
print(name.center(10))
print(name.count('J'))
print(name.endswith('!'))
print(name.endswith('!', 10, 11))
print(name.find('!'))
print(name.index('ohn'))

name = 'JohnDon'

print(name.isalnum())
print(name.isalpha())

name = 'ohz'

print(name.islower())
print(name.isprintable())

name = ' '

print(name.isspace())

name = "World Health Organaization"

print(name.istitle())
print(name.startswith('World'))
print(name.swapcase())

name = 'ohz'

print(name.title())