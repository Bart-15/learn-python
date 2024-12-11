'''
Write a function that requires an indefinite number of
arguments. What this function must do is return True if at any
time the number zero has been entered twice consecutively.

For example:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
'''

def has_consecutive_zeros(*args):
  total_zeros = 0

  for value in args:
    if value == 0:
      total_zeros += 1

  return True if total_zeros == 2 else False


result = has_consecutive_zeros(5,6,1,0,0,9,3,5)
print(result)


