# setting up the modules to "import" in python:
from sys import argv

# input the "filename":
script, filename = argv

#this will open the file which you just inpu the "filename" of:
txt = open(filename)

print "Here is your file %r:" % filename
print txt.read()

print "Type the filename again:"

# give the value to file_again:
file_again = raw_input(">")

# open the file whose name is "file_again":
txt_again = open(file_again)

#??
print txt_again.read()

# ??
txt.close()
txt_again.close()
