from flask import Flask
app = Flask(__name__)

@app.route("/")
def model():
    ptype = raw_input("Project Type: ")
    size = int(raw_input("Size: "))
    rainfall = int(raw_input("Annual Rainfall (Inches): "))
    retained = int(raw_input("Percent of Stormwater Retained: "))
    cost_per_size = 15.75


    print "Runoff Reduced and Costs: \n"
    total_reduction = size*rainfall*retained*144*0.00433
    print "Total Annual Runoff Reduction (Gallons): %r \n" % total_reduction
    total_construction = size*cost_per_size
    print "Total Construction Cost: %r \n" % total_construction
    print "Annual Maintenance Cost: $60"

if __name__ == "__main__":
    app.run()
