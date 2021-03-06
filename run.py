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
  cur = con.execute('SELECT DISTINCT style FROM rides')
  for row in cur:
    trails.append(list(row))

  return render_template('landing.html', trails=trails)


@app.route('/alllocation')
def alllocations():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT location FROM rides')
  for row in cur:
    ride.append(list(row))

  return render_template('alllocation.html', ride=ride)



@app.route('/Canterbury/result')
def Cantlocation():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail , img, difficulty, distance, style, location FROM rides WHERE location="Canterbury"')

  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)



@app.route('/Tasman/result')
def Tasmanlocation():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail , img, difficulty, distance, style, location FROM rides WHERE location="Tasman"')

  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)

@app.route('/Wellington/result')
def Wellylocation():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail , img, difficulty, distance, style, location FROM rides WHERE location="Wellington"')

  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)




@app.route('/Bay of Plenty/result')
def Baylocation():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail , img, difficulty, distance, style, location FROM rides WHERE location="Bay of Plenty"')

  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)


@app.route('/Rotorua/result')
def Rotolocation():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail , img, difficulty, distance, style, location FROM rides WHERE location="Rotorua"')

  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)



@app.route('/Otago/result')
def Otagolocation():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail , img, difficulty, distance, style, location FROM rides WHERE location="Otago"')

  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)



@app.route('/West Coast/result')
def Westlocation():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail , img, difficulty, distance, style, location FROM rides WHERE location="West Coast"')

  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)






@app.route('/Heaphy/result')
def Heaphy():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail , img, difficulty, distance, style, location FROM rides WHERE trail="The Heaphy track"')

  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)




@app.route('/Wakamarina/result')
def Wakamarina():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail , img, difficulty, distance, style, location FROM rides WHERE trail="Wakamarina track"')

  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)



@app.route('/Coronetpeak/result')
def coropeak():
  ride = []
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT DISTINCT description, trail , img, difficulty, distance, style, location FROM rides WHERE trail="Coronet Peak"')

  for row in cur:
    ride.append(list(row))

  return render_template('result.html', ride=ride)





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
