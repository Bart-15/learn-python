import os  

file = open('sample.txt', 'w')
file.write('test hello bart')

file.close()

print(os.listdir())