from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = '9970436dddec6e16b82c62475435623fdbe7fa03'

# to run:
# cd to directory
# source env/bin/activate
# export FLASK_APP=run.py; export FLASK_DEBUG=1
# flask run

MENUDB = 'demo.db'




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/landing')
def landing():
  trails = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT style, img FROM links')
  for row in cur:
    trails.append(list(row))

  return render_template('landing.html', trails=trails)


@app.route('/jumps/location')
def jump():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT location, style FROM rides WHERE style="jumps"')
  for row in cur:
    ride.append(list(row))

  return render_template('location.html', ride=ride)


@app.route('/singletrack/location')
def singletrack():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT location, style FROM rides WHERE style="singletrack"')
  for row in cur:
    ride.append(list(row))

  return render_template('location.html', ride=ride)




@app.route('/technical/location')
def technical():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT location, style FROM rides WHERE style="technical"')
  for row in cur:
    ride.append(list(row))

  return render_template('location.html', ride=ride)



@app.route('/Long Rides/location')
def Longrides():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT location, style FROM rides WHERE style="Long Rides"')
  for row in cur:
    ride.append(list(row))

  return render_template('location.html', ride=ride)




@app.route('/Forests/location')
def Forests():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT location, style FROM rides WHERE style="Forests"')
  for row in cur:
    ride.append(list(row))

  return render_template('location.html', ride=ride)




@app.route('/Alpine/location')
def Alpine():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT location, style FROM rides WHERE style="Alpine"')
  for row in cur:
    ride.append(list(row))

  return render_template('location.html', ride=ride)



@app.route('/Seaside/location')
def seaside():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT location, style FROM rides WHERE style="Seaside"')
  for row in cur:
    ride.append(list(row))

  return render_template('location.html', ride=ride)



@app.route('/bikepark/location')
def bikepark():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT location, style FROM rides WHERE style="bikepark"')
  for row in cur:
    ride.append(list(row))

  return render_template('location.html', ride=ride)





@app.route('/singletrack/Tasman/result')
def singleresult():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail , img, difficulty, distance, style, location FROM rides WHERE location="Tasman" AND style="singletrack"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)




@app.route('/singletrack/Otago/result')
def singleresultOtago():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Otago" AND style="singletrack"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)






@app.route('/singletrack/Canterbury/result')
def singleresultCanterbury():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Canterbury" AND style="singletrack"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)







@app.route('/singletrack/Wellingotn/result')
def singleresultWellington():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Wellington" AND style="singletrack"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)







@app.route('/jumps/Tasman/result')
def jumpsT():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Tasman" AND style="jumps"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)








@app.route('/jumps/Bay of Plenty/result')
def jumps():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Bay of Plenty" AND style="jumps"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)








@app.route('/jumps/Canterbury/result')
def jumps1():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Canterbury" AND style="jumps"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)







@app.route('/jumps/Tasman/result')
def jumps2():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Tasman" AND style="jumps"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)






@app.route('/jumps/Otago/result')
def jumps3():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Otago" AND style="jumps"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)







@app.route('/jumps/Wellington/result')
def jumps4():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Wellingotn" AND style="jumps"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)






@app.route('/jumps/Rotorua/result')
def jumps5():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Rotorua" AND style="jumps"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)









@app.route('/bikepark/Canterbury/result')
def bikepark1():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Canterbury" AND style="bikepark"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)







@app.route('/bikepark/Tasman/result')
def bikeparkTasman():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Tasman" AND style="bikepark"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)






@app.route('/bikepark/Bay of Plenty/result')
def bikeparkBOF():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Bay of Plenty" AND style="bikepark"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)






@app.route('/bikepark/Otago/result')
def bikeparkOtago():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Otago" AND style="bikepark"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)







@app.route('/bikepark/Wellington/result')
def bikeparkWelly():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Wellington" AND style="bikepark"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)






@app.route('/technical/Wellington/result')
def technicalWelly():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Wellington" AND style="technical"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)






@app.route('/technical/Tasman/result')
def technicalTasman():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Tasman" AND style="technical"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)





@app.route('/technical/Rotorua/result')
def technicalRoto():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Rotorua" AND style="technical"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)





@app.route('/Alpine/Tasman/result')
def AlpineTasman():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Tasman" AND style="Alpine"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)




@app.route('/Alpine/West Coast/result')
def AlpineWestCoast():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="West Coast" AND style="Alpine"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)






@app.route('/Alpine/Otago/result')
def AlpineOtago():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Otago" AND style="Alpine"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)







@app.route('/Seaside/Tasman/result')
def SeasideTasman():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Tasman" AND style="Seaside"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)









@app.route('/Forests/Tasman/result')
def ForestsTasman():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Tasman" AND style="Forests"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)





@app.route('/Forests/West Coast/result')
def ForestsWest():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="West Coast" AND style="Forests"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)



@app.route('/Forests/Rotorua/result')
def ForestsRoto():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Rotorua" AND style="Forests"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)







@app.route('/Long Rides/Rotorua/result')
def LongRoto():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Rotorua" AND style="Long Rides"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)





@app.route('/Long Rides/West Coast/result')
def LongWest():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="West Coast" AND style="Long Rides"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)










@app.route('/Long Rides/Tasman/result')
def LongTasman():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides WHERE location="Tasman" AND style="Long Rides"')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)









@app.route('/all/result')
def all():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail, img, difficulty, distance, style, location FROM rides ')
  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)













@app.route('/about')
def about():
    ride = []
    con = sqlite3.connect(MENUDB)
    cur = con.execute('SELECT photo FROM photos ')
    for row in cur:
      ride.append(list(row))

    return render_template('about.html', ride=ride)



@app.route('/contact')
def contact():
    return render_template('contact.html')





'''
def fetchMenu(con):
  burgers = []
  free = '0'
  cur = con.execute('SELECT burger,price FROM burgers WHERE price>=?', (free,))
  for row in cur:
    burgers.append(list(row))

  drinks = []
  cur = con.execute('SELECT drink,price FROM drinks')
  for row in cur:
    drinks.append(list(row))

  sides = []
  cur = con.execute('SELECT side,price FROM sides')
  for row in cur:
    sides.append(list(row))

  return {'burgers':burgers, 'drinks':drinks, 'sides':sides}

@app.route('/')
def index():
  con = sqlite3.connect(MENUDB)
  menu = fetchMenu(con)
  con.close()
  return render_template('index.html', disclaimer='may contain traces of nuts', burgers=menu['burgers'], drinks=menu['drinks'], sides=menu['sides'])

@app.route('/order')
def order():
  con = sqlite3.connect(MENUDB)
  menu = fetchMenu(con)
  con.close()
  return render_template('order.html', burgers=menu['burgers'], drinks=menu['drinks'], sides=menu['sides'])

@app.route('/confirm', methods=['POST'])
def confirm():
  details = {}
  items = {}

  for input in request.form:
    if input == 'name' or input == 'address':
      details[input] = request.form[input]
    elif request.form[input] and request.form[input] != '0':
      items[input] = request.form[input]

  con = sqlite3.connect(MENUDB)
  cur = con.execute( 'INSERT INTO orders(name, address, items) VALUES(?, ?, ?)', (details['name'], details['address'], str(items)) )
  con.commit()
  con.close()

  return render_template('confirm.html', details=details, items=items)

@app.route('/vieworder/<order_id>')
def viewOrder(order_id):
  if 'username' in session:
    con = sqlite3.connect(MENUDB)
    cur = con.execute('SELECT * FROM orders WHERE id=?', (order_id,))
    order = cur.fetchone()
    con.close()
    return str(order) + ' user: ' + session['username']
  else:
    return redirect(url_for('login')) #render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST' and request.form['username'] == 'admin':
    session['username'] = request.form['username']
    return redirect(url_for('panel'))
  else:
    return render_template('login.html')

@app.route('/panel')
def panel():
  orders = []
  if 'username' in session:
    con = sqlite3.connect(MENUDB)
    cur = con.execute('SELECT * FROM orders')
    for row in cur:
      orders.append(list(row))
    con.close()
    return render_template('panel.html', orders=orders)
  else:
    return render_template('login.html')

@app.route('/logout')
def logout():
  if 'username' in session:
    session.pop('username', None)
  return redirect(url_for('index'))
'''
