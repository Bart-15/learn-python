names = ['Max', 'Bruce', 'Tony']
age = [22,21,23]

combination = (zip(names, age))

print(combination)

for name, age in combination:
  print(f'{name} is {age} years old.')