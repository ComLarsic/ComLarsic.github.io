from flask import *


app = Flask(__name__)
Home = "/"


#Website routes
@app.route(Home)
def home():
    return render_template('home.html')




if (__name__ == "__main__"):
    app.run(debug=True)
app.run(host='0.0.0.0', port=8080)