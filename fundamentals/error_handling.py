def addition():
  try:
    # The code you want to check
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    print(n1 + n2)
    print("Thanks for adding")
  except TypeError:
    # Execite if there is an error
    print('You are trying to concatenate different type')
  except ValueError:
    print("This is not a number")
  
  else:
    # Code that will be executed if there is no error
    print('You did great!')

  finally:
    # The code that will be executed anyway
    print('That\'s all')


def ask_number():
  while True:

    try:
      number = int(input("Enter a number: "))
    except:
      print('This is not a number')
    else: 
      print(f"You have enter {number}")
      break

  print('Thank you boss!')

ask_number()