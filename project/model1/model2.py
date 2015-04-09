
area = raw_input("Community Area: ")

print """
Please choose from the folloing type codes:
1. Rain Gardens
2. Biosweasl
3. Landscaped Sidewalks
...

"""
ptype = raw_input("Project Type: ")

# if ptype = 1
# percents = 40
# else if ptype = 2
# percents = 50
# else if ptype = 3
# percents = 60

size = int(raw_input("Size: "))
# To show the model tailored to particular projects:
percents = int(raw_input("Percent of the size that you want to control: "))
rainfall = int(raw_input("Annual Rainfall (Inches): "))
retained = int(raw_input("Percent of Stormwater Retained: "))
cost_per_size = 15.75


print "Runoff Reduced and Costs: \n"
total_reduction = size*rainfall*retained*144*0.00433* (100 - percents)/100
print "Total Annual Runoff Reduction (Gallons): %r \n" % total_reduction
total_construction = size*cost_per_size
print "Total Construction Cost: %r \n" % total_construction
print "Annual Maintenance Cost: $60"
