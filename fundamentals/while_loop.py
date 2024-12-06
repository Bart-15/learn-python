coins = 5

while coins > 0:
  print(f'I have {coins} coins')
  coins = coins - 1
else: 
  print('I have no money anymore')


answer = 'y'

while answer == 'y':
  answer = input('Do you want to continue? (y/n)')
else: 
  print('Thank you!')