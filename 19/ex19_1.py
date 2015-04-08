def num_schools(num_applied, num_waitlisted, num_rejected, num_admitted):
    print "Kai has applied %d schools." % num_applied
    print "Kai has got %d schools waitlistd." % num_waitlisted
    print "Kai got %d schools rejected." % num_rejected
    print "Do you know how many school Kai got the offer? It's %d." % num_admitted
    print "That's too much work! \n"


print "We can assign numbers to the functions."
num_schools(9, 2, 5, 2)

num_schools(9 - 1 + 1, 2, 5, 2)

thefunction = num_schools

thefunction(1, 1, 1, 1)

print "Or, we can assign values"
