'''
  This function accepts 2 inputs on user to create a funny beer brand name 
'''

def generateBeerBrand():
  question1 = input('Name of your pet? ')
  question2 = input('Name of your favorite food? ')

  return print(f'The beer brand is: "{question1} {question2}"')

generateBeerBrand()