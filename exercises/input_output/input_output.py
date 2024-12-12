text_file = open("sample.txt")

first_line = text_file.readline()
second_line = text_file.readline()
third_line = text_file.readline()

print(first_line)
print(second_line)
print(third_line)

text_file.close()