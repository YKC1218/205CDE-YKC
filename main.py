from flask import Flask, render_template, redirect, url_for, request, session, flash
import pymysql
from flask_wtf import Form
from wtforms import TextField, IntegerField, SubmitField
from wtforms import validators, ValidationError




app = Flask(__name__)
app.secret_key = 'Any string'

db = pymysql.connect("localhost","root","136723","user")


@app.route("/customer" ,methods = ['GET', 'POST'])
def contact():


	if request.method == 'POST':


		UserN = request.form["Name"]
		EmA = request.form["Email"]
		PnE = request.form["Phonenumber"]
		cursor = db.cursor()
		cursor.execute("""UPDATE user SET Name=%s, Email=%s, Phone=%s WHERE username=%s""", (UserN, EmA, PnE,session['usern']))
		db.commit()
		flash('input personal data successfully')

		

	cursor = db.cursor()
	cursor.execute("""SELECT Name,Email,Phone FROM user WHERE username =%s""",session['usern'])	
	results = cursor.fetchall()
	return render_template('contact.html' , R1 = results)
	db.close()


@app.route("/login", methods=['POST', 'GET'])
def login():
	error = None
	if request.method == 'POST':
		usrname = request.form["username"]
		pwd = request.form["password"]
		cursor = db.cursor()
		sql1 = ("SELECT username, password FROM user WHERE username = '"+usrname+"'AND password = '"+pwd+"'" )
		cursor.execute(sql1)
		db.commit()		
		results = cursor.fetchall()

		for row in results:
			custName = row[0]
			custPassword = row[1]
			session['usern'] = custName	

			if custName == usrname and custPassword == pwd :								
				if usrname == 'admin' and pwd =='admin':
					session['type'] = "dashboard"
					flash('logged in')
					session['loggedin'] = True
					return redirect(url_for("index"))
					return render_template("index.html")
				else:
					session['type'] = "customer"
					session['loggedin'] = True
					flash('logged in')
					return redirect(url_for("index"))
					return render_template("index.html")

		else:
			session['loggedin'] != True
			session['type'] = "login"
			flash('Incorrect username or password')
	return  render_template("login.html" )

@app.route("/logout")
def logout():
	session.pop('usern', None)
	session['type'] = "login"
	flash('logged out')
	return redirect(url_for("index"))

@app.route("/Signup", methods=['POST','GET'])
def signup():
	error = None
	if request.method == 'POST':
		Newus = request.form["username"]
		Newp  = request.form['password']

		cursor = db.cursor()
		sql=("""SELECT username FROM user""")
		cursor.execute(sql)
		db.commit()
		results = cursor.fetchall()
		for row in results:
			custName = row[0]	
			if Newus == custName:
				flash(' repeated username ')
				break
		else:		
			cursor.execute("""INSERT INTO user (username, password) VALUES (%s, %s)""", (Newus,Newp))
			db.commit()
			flash(' registered successfully')
	return render_template('signup.html', error = error)
	
	db.close()	


@app.route("/index")
@app.route("/")
def index():
	return render_template("index.html")



			
@app.route("/dashboard", methods=['POST', 'GET'])
def dashboard():
	error = None
	if request.method == 'POST':		
		productn = request.form["productname"]
		productsize = request.form["productsize"]
		productprice = request.form["productprice"]
		productqty = request.form["productqty"]
		productimage = request.form["productimage"]
		cursor = db.cursor()
		render_template("dashboard.html")
			

		cursor.execute("""INSERT INTO product (product_name,product_size,product_price,product_qty,product_image) VALUES (%s,%s,%s,%s,%s)""",(productn,productsize,productprice,productqty,productimage))
		db.commit()
		flash('new product added')
		return redirect(url_for("index"))
		cursor.execute("""SELECT * FROM product""")

		db.commit()		
		al12 = cursor.fetchall()			
	else:

		cursor = db.cursor()
		cursor.execute("""SELECT * FROM product""")

		db.commit()

		al12 = cursor.fetchall()
			

	return  render_template("dashboard.html", products = al12)



@app.route("/addtocart" , methods=['POST', 'GET'])
def add():
	if request.method == 'POST':
		pname= request.form["shopproduct"]
		psize= request.form["pSize"]
		pQty= request.form["pQty"]
		cursor = db.cursor()

		cursor.execute("SELECT product_price FROM product WHERE product_name = %s",pname)
		db.commit()
		price = cursor.fetchall()
		uname = session['usern']
								
		
		sql1= "INSERT INTO shoppingcart VALUES(%s,%s,%s,%s,%s)"
		value = (uname, pname , psize, pQty, price)
		cursor.execute(sql1,value)
		db.commit()
		flash('added to cart')
		return redirect(url_for("index"))

		cursor.execute("""SELECT * FROM product""")

		db.commit()
		p1 = cursor.fetchall()
		
	else:
		if session['type'] =="login" :			
			flash('login first!')	
			return redirect(url_for("index"))			
						
		cursor = db.cursor()
		cursor.execute("""SELECT * FROM product""")

		db.commit()

		p1 = cursor.fetchall()
				
			

	return render_template("products.html", all = p1)

@app.route("/Aboutus")
def about():
	return render_template("Aboutus.html")

@app.route("/ShoppingCart" , methods=['POST', 'GET'])
def cart():
	error = None
	if request.method == 'POST':
	

		cursor = db.cursor()
		cursor.execute("SELECT s_product_name,product_size,product_price,product_quantity,shoppingcart_user_name FROM shoppingcart WHERE shoppingcart_user_name =%s",session['usern'])
		db.commit()		
		cartproducts = cursor.fetchall()
		for row in cartproducts:
			PDN = row[0]
			PDS = row[1]
			PDP = row[2]
			PDQ = row[3]
			user = row[4]
			if row[4] == session['usern']:
				sql6=("INSERT INTO uorder (order_user_name,orderproducts,orderproductQTY,order_product_size,product_price) VALUES (%s,%s,%s,%s,%s)")
				value = (user,PDN,PDQ,PDS,PDP)
				cursor.execute(sql6,value)
				db.commit()

				fla = True
		if fla == True:
			flash('added to order')
			cursor.execute("DELETE FROM shoppingcart WHERE shoppingcart_user_name =%s",session['usern'])
			db.commit()

		cursor.execute("SELECT FORMAT(SUM(product_price*product_quantity),0) FROM  shoppingcart WHERE shoppingcart_user_name =%s",session['usern'])
		db.commit()
		price = cursor.fetchall()
		price2 = price*1	

		cursor = db.cursor()

		return redirect(url_for("index"))	

	else:
		if session['type'] =="login" :			
			flash('login first!')	
			return redirect(url_for("index"))	
		cursor = db.cursor()
		cursor.execute("SELECT s_product_name,product_size,product_price,product_quantity FROM shoppingcart WHERE shoppingcart_user_name =%s",session['usern'])
		db.commit()		
		cartproducts = cursor.fetchall()

		cursor.execute("SELECT FORMAT(SUM(product_price*product_quantity),0) FROM  shoppingcart WHERE shoppingcart_user_name =%s",session['usern'])
		db.commit()
		price = cursor.fetchall()
		price2 = price*1		



		
		
	return render_template("shoppingcart.html",shopcart=cartproducts, price=price2)







@app.route("/Contactus")
def contactus():
	return render_template("Contactus.html")





if __name__=='__main__':
	app.debug = True
	app.run(host="0.0.0.0", port=8000)
