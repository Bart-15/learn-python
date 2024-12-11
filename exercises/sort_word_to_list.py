'''
Write a function (you can name it whatever you want) that
takes any word as a parameter, and returns all of its unique
letters (without repetition) in alphabetical order.
For example, if when calling this function we pass the word
"entertaining", it should return ['a', 'e', 'g', 'i', 'n', 'r', 't']
'''

def sort_word_to_list(word):
  letters = list(dict.fromkeys(word))

  return sorted(letters)

result = sort_word_to_list('entertaining')
print(result)