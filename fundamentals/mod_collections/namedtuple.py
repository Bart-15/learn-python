from collections import namedtuple

Dog = namedtuple('Animal', ['name','age'])

dog1 = Dog('Max', 12)

print(dog1[0])