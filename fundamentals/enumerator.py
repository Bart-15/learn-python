my_list = ['a','b','c']

for index, item in enumerate(my_list):
  print(index, item)


for index, item in enumerate(range(1, 11)):
  print(index, item)


my_tuples = list(enumerate(my_list))

print(my_tuples)
