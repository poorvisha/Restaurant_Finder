    # All Imports
from flask import Flask, render_template, request
import pymysql
import json


app = Flask(__name__)

# Configurations
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='restaurant_finder')
cursor = conn.cursor()


# The Home Page
@app.route('/')
def main():
    return render_template('index.html')


# To Show the List of Restaurants
@app.route('/showRestaurant_List',methods=['GET', 'POST'])
def showRestaurant_List():
    selected_city = request.form['city']
    return render_template('restaurant_list.html',city=selected_city)


# Get the List of restaurants from the db and send.
@app.route('/restaurant_list',methods=['GET','POST'])
def restaurant_List():
    cityName = request.args.get('city')
    sql = "select restaurant_name,rest_id,cuisine,restaurant_address1,restaurant_address2,contact_number, zipcode from restaurant_detail where city = '"+cityName+"'"
    cursor.execute(sql)
    columns = [desc[0] for desc in cursor.description]
    result = []
    rows = cursor.fetchall()
    for row in rows:
        row = dict(zip(columns, row))
        row['restaurant_address1'] = row['restaurant_address1'] + ",</br>" +cityName +", CA "+row['zipcode']
        result.append(row)
    data = json.dumps(result)
    return data


# Show a particular restaurant menu page.
@app.route('/showRestaurant_Menu')
def showRestaurant_Menu_():
    # Get the restaurant_id what the user has selected
    global restid
    restid = request.args.get('restid')

    # Query to get the name of the restaurant
    sql = "select restaurant_name from restaurant_detail where rest_id = " + restid
    cursor.execute(sql)

    # Get the rows from the resultset
    rows = cursor.fetchone()
    rest_name = rows[0]

    #Display the restaurant menu page.
    return render_template("restaurant_menu.html", retid = rest_name)


# Get the Menu items of the selected restaurant from the db and pass it to the restaurant_menu page.
@app.route('/restaurant_Menu',methods=['GET','POST'])
def restaurant_Menu():

    # Query to get the menu items from the db for the selected restaurant.
    sql = "select food_item_name, food_item_id, price from restaurant_menu_detail where rest_id = "+ restid

    # Execute the query from db.
    cursor.execute(sql)

    # Need column names of db to use it on dataTable jquery.
    columns = [desc[0] for desc in cursor.description]
    resultSet = []
    rows = cursor.fetchall()

    # Iterate through rows and create a dictionary object and add it to List
    for row in rows:
        row = dict(zip(columns, row))
        resultSet.append(row)
     # Convert the list to json and pass it on to Restaurant Menu page
    data = json.dumps(resultSet)
    return(data)


# Shows Add To cart page.
@app.route('/showAddToCart',methods=['GET','POST'])
def showAddToCart():
    # Fetch the menu items selected by the user.
    global result
    result = dict(request.form)

    global quantityList
    quantityList = result['Quantity']

    global checkedIdSet
    checkedIdSet = result['checkbx'];

    return render_template("AddCart.html")


# Display the menu items with quantity and price on the add To Cart page.
@app.route('/addToCart', methods=['GET','POST'])
def addToCart():

    resultSet = []
    count = -1

    # Iterate through the Checked Food Items and get its details from the database
    for food_item in checkedIdSet:
        count = count+1

        cursor.execute("Select food_item_name, price from restaurant_menu_detail where rest_id = %s and food_item_id = %s",(int(restid), int(food_item)))
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        columns.append('quantity')
        columns.append('totalprice')

        # Create dictionary of columns and row.
        for row in rows:
            row = dict(zip(columns, row))
            row['quantity'] = quantityList[count]
            row['totalprice'] = round(row['price'] * float(quantityList[count]),2)
            resultSet.append(row)

    data = (json.dumps(resultSet))
    return(data)


# On Confirmation of AddToCart, display customer detail page.
@app.route('/showCustomerDetail', methods=['GET', 'POST'])
def showCustomerDetail():
    global _bill_totalprice
    _bill_totalprice = request.form['totprice']
    return render_template("CustomerDetail.html")


# Get the customers details and store it on db.
@app.route('/addCustomerDetail', methods=['GET', 'POST'])
def addCustomerDetail():

    # Customer Details
    _name = request.form['fname']
    _lname = request.form['lname']
    _mobile = request.form['mobile']
    _address1 = request.form['address1']
    _address2 = request.form['address2']
    _email = request.form['email']
    _city = request.form['city']
    _state = 'california'
    _zip = request.form['zip']

    # Insert into db.
    cursor.execute("INSERT INTO billing_detail (cust_name, cust_address1, cust_address2, cust_city, cust_state, cust_zipcode, cust_contact_number, restaurant_id, total_price, email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (_name, _address1, _address2, _city, _state, _zip, _mobile, restid, float(_bill_totalprice),_email))

    cursor.execute("select max(billing_id)  from billing_detail where email = %s and restaurant_id = %s"  ,(_email, int(restid)))
    row = cursor.fetchone()
    billing_id = row[0]

    count = -1
    # Insert food items in database.
    for food_item in checkedIdSet:
        count = count + 1
        cursor.execute("INSERT INTO ordered_item_detail(billing_id, food_item_id, food_item_qty) VALUES (%s, %s, %s)",(billing_id, food_item, quantityList[count]))
    conn.commit()
    orderid = "00000"+ str(billing_id)
    return render_template("Thankyou.html", customerid = orderid)



# Application starting point.
if __name__ == '__main__':
    app.run()
