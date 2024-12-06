import time
from random import randint


def guess_the_number():
  secret_number = randint(1, 100)
  max_attempts = 8
  attempts = 0

  guess = None

  print("⭐Welcome to 'Guess the Number'!⭐")
  print("I have selected a number between 1 and 100. Can you guess what it is? 👀")
  time.sleep(1)
  print("You have a maximum of 8 tries! Good luck 🚀")

  while attempts < max_attempts:
    try:
      guess = int(input('Enter your guess: '))

      attempts += 1

      match guess:
        case _ if guess < 1 or guess > 100:
          print('You chosen a number out of play')
        case _ if guess < secret_number:
          print('You choose a lower than the secret number')
        case _ if guess > secret_number:
          print('You choose a higher number than the secret number')
        case _ if guess == secret_number:
          print(f"Congratulations! You guessed the number {secret_number} correctly!")
          break
        case _:
          print('Please input a valid number')
    except ValueError:
      print("Invalid input. Please enter a valid number")

  if attempts == max_attempts:
    print(f"Sorry, you've reached the maximum number of attempts. The number was {secret_number}.")
        

guess_the_number()


