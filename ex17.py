from sys import argv
from os.path import exists
#import argv ang exists
script, from_file, to_file = argv
# copy from one file to another
print(f"Copying from {from_file} to {to_file}")
#open creates file object and stores in variable
in_file = open(from_file)
#read returns the contents of the file into the variable
indata = in_file.read()

print(f"The input file is {len(indata)} long")

print(f"does the output file exist? {exists(to_file)}")
input("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

#open to_file in write mode (blank when opened in "w"), saves variable
out_file = open(to_file, "w")
#writes contents of indata to out_file.
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
