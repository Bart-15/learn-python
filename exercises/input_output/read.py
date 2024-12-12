''' 
  It reads only the text file
'''

text_file = open("test1", 'r')

text_file.write('hello') # will not work because its not writable

print(text_file.read()) # will work

text_file.close()