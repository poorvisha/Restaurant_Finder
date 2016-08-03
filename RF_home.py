import os
import pickle

from flask import *
from pymongo import MongoClient

app = Flask(__name__)

# Session secret key for passing cityname from homepage to next cities page
app.secret_key = "finder"


# Render home html template
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        return render_template("index.html")

    try:
        # If user selects any city name from selection box
        if request.method == "POST":
            session['city_name'] = request.form['city_name']
            return redirect(url_for('/navbar.html'))
    except Exception as e:
        print(e)


# Remove the "debug=True" for production
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))

    app.run(host='localhost', port=port, debug=True)
