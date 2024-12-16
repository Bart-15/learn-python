'''
By using 'a' 9it will add  a new text at the very last of the word
'''

text_file = open("test1.txt", 'a')

text_file.write('Yay! Congratulations')

text_file.close()

'Sample scenario if you want to add a list of word with new line'

def word_new_line():
  text_file = open("test1.txt", 'a')
  list_words = ["python", "developer", "hangman", "programming", "challenge"]

  for word in list_words:
    text_file.write(f'{word} \n')

  text_file.close()

word_new_line()