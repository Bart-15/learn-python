from os import system, name

def clear():

  # for windows
  if name == 'nt':
    _ = system('cls')
  # for mac and linux
  else:
    _ = system('clear')

def introduction():
  input_name = input('What is your name?: ')
  input_age = int(input('What is your age?: '))
  clear()

  print(f'My name is {input_name} and I\'m {input_age} yrs old.')


introduction()


