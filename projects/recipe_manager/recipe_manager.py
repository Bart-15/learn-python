from os import system, name
from pathlib import Path

recipes_path = Path('recipes')

def clear():

  # for windows
  if name == 'nt':
    _ = system('cls')
  # for mac and linux
  else:
    _ = system('clear')

def count_recipes(path):
  counter = 0
  for path in Path(path).glob('**/*.txt'):
    counter += 1

  return counter


def start():
  clear()
  print('*' * 50)
  print('Welcome to the recipe app manager')
  print('*' * 50)

  total_recipes = count_recipes(recipes_path)
  print(f'The recipes are inside of {recipes_path} folder')
  print(f'Total recipes: {total_recipes}')

  menu_choice = 'x'

  while not menu_choice.isnumeric() or int(menu_choice) not in range(1, 7): 
    print('Choose an option: ')
    print('''
    [1] - Read recipe
    [2] - Create new recipe
    [3] - Create new category
    [4] - Eliminate recipe
    [5] - Eliminate category
    [6] - Leave the program
     ''')
    menu_choice = input()

  return menu_choice

start()