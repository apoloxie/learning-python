from flask import Flask
app = Flask(__name__)

@app.route("/ex9")
def ex9():

    # Here's some new strange stuff, remember type it exactly.

    days = "Mon Tue Wed Thu Fri Sat Sun"
    months = "Jan<br>Feb<br>Mar<br>Apr<br>May<br>Jun<br>Jul<br>Aug"

    thestring = "Here are the days: " + days + "<br>"
    thestring += "Here are the months: " + months + "<br>"

    thestring += """
There's something going on here.<br>
With the three double-quotes.<br>
We'll be able to type as much as we like.<br>
Even 4 lines if we want, or 5, or 6.<br>
"""
    print 'wolf is using print here'
    return thestring

if __name__ == "__main__":
    app.run(debug=True)
