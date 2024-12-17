from collections import defaultdict

# Will print this if key dictionary is not available 
my_dict = defaultdict(lambda: 'hehehe') 

my_dict['name'] = 'Bart'
my_dict['last_name'] = 'Tabusao'

print(my_dict['hello'])
