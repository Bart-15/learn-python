'''
Create a function called return_distincts() that receives 3
integers as parameters.
If the sum of the 3 numbers is greater than 15, it must return
the highest number.
If the sum of the 3 numbers is less than 10, it must return the
lowest number.
If the sum of the 3 numbers is a value between 10 and 15
(included), then it must return the number with the
intermediate value.
'''

def return_distinct(n1, n2, n3):
  base_number = 15
  list = [n1, n2, n3]
  total = sum(list)

  if total > 15:
    return max(list)
  elif total < 10:
    return min(list)
  elif 10 <= total <= 15:
    sorted_numbers = sorted(list)
    return sorted_numbers[1]



result = return_distinct(1,2,17)
print(result)