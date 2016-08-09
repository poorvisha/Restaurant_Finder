import os
from flask import *
from flask import Flask, render_template
import pymysql.cursors
#from pymongo import MongoClient

app = Flask(__name__)

#mysql = PyMySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'welcome'
app.config['MYSQL_DATABASE_DB'] = 'restaurant_finder'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


conn = pymysql.connect(host='localhost', user='root', password='welcome',db='restaurant_finder')

cur= conn.cursor()


app = Flask(__name__)

# Session secret key for passing cityname from homepage to next cities page
app.secret_key = "finder"


# Render home html template
@app.route('/', methods=['POST', 'GET'])
def home():
    print('12345')
    if request.method == "GET":
        return render_template("index.html")

    try:
        # If user selects any city name from selection box
        if request.method == "POST":
            #session['city_name'] = request.form['city_name']
            print("123")
            print(request.form['city'])
            return render_template("index.html")
    except Exception as e:
        print(e)

@app.route('/res')
def res():
    return render_template('res.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

# Remove the "debug=True" for production
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))

    app.run(host='localhost', port=port, debug=True)
