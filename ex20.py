from sys import argv

script, input_file = argv
# create function, f is filename
def print_all(f):
	print(f.read())

#create function, seek controls where the pointer is positioned
def rewind(f):
	f.seek(0)

#create function, readline increments each time it is run.
def print_a_line(line_count, f):
	print(line_count, f.readline())

#create variable that opens input file
current_file = open(input_file)

#print command with new line
print("first let's print the whole file \n")

#prints contents of the input file by calling def print_all
print_all(current_file)

#prints string
print("Now lets rewind, kind of like a tape.")

#def rewind which starts at the first point of the input file
rewind(current_file)

#print statement
print("Let's print three lines:")

#creates variable
current_line = 1
#calls function,prints current_line variable,prints line of input file.
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)