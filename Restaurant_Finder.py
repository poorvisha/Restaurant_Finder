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
    try:
        if request.method == "POST":  # If user selects any city name from selection box

            session['city_name'] = request.form['city_name']  # Get the name and assign it to city_name  session

            return redirect(
                url_for('cities'))  # Redirect to cities html template whose contents changes according to selected city
    except Exception as e:
        print(e)

    return render_template("index.html")


# Remove the "debug=True" for production
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))

    app.run(host='localhost', port=port, debug=True)
