from flask import *

#Variables
app = Flask(__name__)
Home = "/"
about = "/about.html"
contact = "/contact.html"
category = "/category.html"
bry = "/brython.html"


#Website routes
@app.route(Home)
def home():
    return render_template('home.html')

@app.route(about)
def about():
    return render_template("about.html")

@app.route(contact)
def contact():
    return render_template("contact.html")

@app.route(category)
def category():
    return render_template("category.html")

@app.route(bry)
def bry():
    return render_template('brython.html')


#Run
if (__name__ == "__main__"):
    app.run(debug=True)
app.run(host='0.0.0.0', port=8080)