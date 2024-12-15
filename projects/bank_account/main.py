class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

class Customer(Person):
  def __init__(self, first_name, last_name, account_number, balance = 0):
    super().__init__(first_name, last_name)
    self.account_number = account_number
    self.balance = balance

  def __str__(self):
    return f'''
    Client: {self.first_name} 
    Account Number: {self.account_number}
    Account Balance: {self.balance}
    '''
  
  def deposit(self, amt_deposit):
    self.balance += amt_deposit
    print('Deposit accepted!')

  def withdraw(self, amt_withdraw):
    if self.balance >= amt_withdraw:
      self.balance -= amt_withdraw
    else:
      print('Insufficient funds!')

def create_customer():
  first_name = input("Enter your firstname: ")
  last_name = input("Enter your lastname: ")
  account_number = input("Enter your account number: ")

  customer = Customer(first_name, last_name, account_number)

  return customer


def start():
  my_customer = create_customer()
  print(my_customer)

  option = 0

  while option != "E":
    print("Choose: Deposit (D), Withdraw (W), or Exit (E)")
    option = input()

    if option == 'D':
      amt_deposit = int(input('Deposit amount: '))
      my_customer.deposit(amt_deposit)
    elif option == 'W':
      amt_withdraw = int(input('Withdraw amount: '))
      my_customer.withdraw(amt_withdraw)

  print('Thank you for using my Bank Account App - Bart Tabusao')

start()
