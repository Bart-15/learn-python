
'''
  This simple project handles the total commission of a user, based on the rate provided
'''

def calculate_commission(rate):
  name = input('What is your name?: ')
  sales = int(input('Please input your total month sales: '))

  total_commission = round(sales * rate / 100, 2)

  print(f'Hi {name}, your total commissions for this month is ${total_commission}\nCongratulations!')

calculate_commission(13)