# Loop through the numbers 1 to 100 and print out all the odd numbers. You can tell a number is odd by doing number % 2 == 1 

for number in range(1, 101):
  if number % 2 == 1:
    print('odd number:', number)