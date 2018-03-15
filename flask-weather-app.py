from flask import Flask,url_for,render_template,request
from process import Logic

app = Flask(__name__)

@app.route('/')
def abc():
    return render_template('main.html')

@app.route('/weather',methods=['POST','GET'])
def weather():
    proces = Logic()
    city = request.form['city']
    p=proces.query(city)
    if p:
        Today = proces.today()
        Todate = proces.todate()
        cty = proces.item(6, 'city')
        country = proces.item(6, 'country')
        region = proces.item(6, 'region')
        Temp = str(proces.item(4, 'temp'))
        Humidity = str(proces.item(1, 'humidity'))
        Speed = str(proces.item(0, 'speed'))
        Winddirection = str(proces.degtocompass(int(proces.item(0, 'direction'))))
        sunrise = str(proces.item(2, 'sunrise'))
        sunset = str(proces.item(2, 'sunset'))
        latitude = str(proces.item(3, 'lat'))
        longitude = str(proces.item(3, 'long'))
        conditions = str(proces.item(4, 'text'))
        code = int(proces.item(4, 'code'))
        forcast0 = proces.forcast(1)
        forcast1 = proces.forcast(2)
        forcast2 = proces.forcast(3)

        return render_template('index.html', today=Today, todate=Todate, city=city, temp=Temp, humidity=Humidity,
                               speed=Speed, winddirection=Winddirection, \
                               lat=latitude, long=longitude, sr=sunrise, ss=sunset, cond=conditions, code=code, \
                               for0=forcast0, for1=forcast1, for2=forcast2, ccity=cty, cnty=country, reg=region)
    else:
        return render_template('error.html', error="404")


if __name__ == '__main__':
    app.run(debug=True)

