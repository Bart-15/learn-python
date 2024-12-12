'''
Be careful using this, it modifies the whole content of a text file :)
If the file is not existing yet, it will create a new file based on the target name you provided
'''

text_file = open('test1', 'w')

text_file.write('HAHAHHA')

text_file.close()