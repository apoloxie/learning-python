from sys import argv

script, first, second, third, fourth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

fourth = raw_input("This is your fourth variable: ")
print fourth

def main(argc, argv):
    return 0

main(len(argv), argv)

#line 1: "import" to add features, and "argv" is "argument variable"
#line 3: "Unpack"
