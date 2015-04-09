from flask import Flask, request
app = Flask(__name__)

@app.route("/model")
def model():
    retstr = """
    <html>
    <head>
    <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
    </head>
    <body>
    <form action="/model2" method="post">
  <div class="form-group">
    <label for="projecttype">Project Type</label>
    <input type="text" class="form-control" name="projecttype" id="projecttype" placeholder="1, 2, 3, ...">
  </div>

  <div class="form-group">
    <label for="rainfall">Rainfall</label>
    <input type="text" class="form-control" name="rainfall" id="rainfall" placeholder="Inches">
  </div>

  <div class="form-group">
    <label for="size">Size</label>
    <input type="text" class="form-control" name="size" id="size" placeholder="Square feet">
  </div>

  <div class="form-group">
    <label for="retained">Retained</label>
    <input type="text" class="form-control" name="retained" id="retained" placeholder="Inches">
  </div>

  <button type="submit" class="btn btn-default" formaction="/model2">Submit</button>
</form></body></html>"""

    return retstr

@app.route('/model2', methods=['POST'])
def model2():
        retstr = """<html><head>
        <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script></head>
<body>"""
        for k in request.form:
            print k
        ptype = request.form['projecttype']
        size = int(request.form['size'])
        rainfall = int(request.form['rainfall'])
        retained = int(request.form['retained'])
        cost_per_size = 15.75

        retstr += "<h1>Runoff Reduced and Costs</h1> <br>"
        total_reduction = size*rainfall*retained*144*0.00433
        retstr += "Total Annual Runoff Reduction (Gallons): %r <br>" % total_reduction
        total_construction = size*cost_per_size
        retstr += "Total Construction Cost: %r <br>" % total_construction
        retstr += "Annual Maintenance Cost: $60 <br>"

        retstr += '</body></html>'

        return retstr

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)
