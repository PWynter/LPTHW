from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's you file {filename}")
print (txt.read())

file_again = input("Type your file name again: > ")

txt_again = open(file_again)

print(txt_again.read())