import time
import operator

to_remove_opts = [',''.''?''()']

full_text = '''
Data preprocessing is an important task in text classification. With the emergence of Python in the field of data science, it is essential to have certain shorthands to have the upper hand among others. This article discusses ways to count words in a sentence, it starts with space-separated words but also includes ways to in presence of special characters as well.
'''

for thing in to_remove_opts:
  full_text = full_text.replace(thing, '')

count_of_words = full_text.lower().split()
print('Counting words, please wait...\n')
time.sleep(1)


print("Count of words in a given sentence:", len(count_of_words))

word_count = {}

for index in range(len(count_of_words)):
  if count_of_words[index] in word_count:
    word_count[count_of_words[index]] += 1
  else: 
    word_count[count_of_words[index]] = 1
  

sorted_count = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)


for word_tuple in sorted_count:
  print(f'{word_tuple[0].capitalize()} - {word_tuple[1]}')

print(f'There are {len(sorted_count)} unique words')