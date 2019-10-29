from flask import *


app = Flask(__name__)
Home = "/"
about = "/about"
contact = "/contact"
category = "/Scategory"


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


if (__name__ == "__main__"):
    app.run(debug=True)
app.run(host='0.0.0.0', port=8080)