
import operator

def text_analyzer():
  to_remove_opts = [',','.','?','()',' ']
  full_text = input('Please enter random words: ')
  inverted_word = full_text.split()

  for thing in to_remove_opts:
    full_text = full_text.replace(thing, '')
  
  #count words
  word_count = full_text.lower().split()

  print('Count of word in a given sentence:', len(word_count))

  letter_count = {}

  letters = list(full_text)

  for idx in range(len(letters)):
    if(letters[idx] in letter_count):
      letter_count[letters[idx]] += 1
    else:
      letter_count[letters[idx]] = 1
  
  sorted_count = sorted(letter_count.items(), key=operator.itemgetter(1), reverse=True)

  for word_tuple in sorted_count:
    print(f'{word_tuple[0].capitalize()} - {word_tuple[1]}')

  # get the first and last letter
  print(f'This is the first letter - {letters[0]}')
  print(f'This is the last letter - {letters[-1]}')

  # Words inverted order
  print(f'Word inverted order: {inverted_word[::-1]}')

  # check if theres a "Python word"
  print(f'Is there a "Python" word?:', "Yes" if "Python" in inverted_word else "No")

text_analyzer()