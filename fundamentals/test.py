import random

def user_input():
  words =  ["python", "developer", "hangman", "programming", "challenge"]
  words_length = len(words)

  selected = ''

  while True:
    try:
      random_choice = int(input(f"Please select a number between 1 and {words_length}: "))

      if 1 <= random_choice <= words_length:
        return words[random_choice - 1]
      else:
        print(f"Invalid input. Please input a number between 1 and {words_length}.")

    except ValueError:
      print("Invalid input. Please enter a numeric value.")



def hangman():
  input_result = user_input()
  guessed_word = ["_"] * len(input_result)

  attempts = 8

  while attempts > 0 and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
      print("Invalid input. Please enter a valid single letter")
      continue

    guessed_word.append(guess)

    if guess in input_result:
      print(f'Yay! Good guess! The letter "{guess}" is in the word.')
      for idx, letter in enumerate(word):
        if letter == guess:
          guessed_word[idx] = guess

    else:
      attempts -= 1
      print(f"Wrong guess. You have {attempts} attempts left.")
    
    print("Current word:", " ".join(guessed_word))

  if '_' not in guessed_word:
    return print(f'Congratulations! You\'ve guessed the word: {word}')
  else:
    print(f"Game over! The word was: {word}")

hangman()