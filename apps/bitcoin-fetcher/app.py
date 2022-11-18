import requests
from apscheduler.schedulers.background import BackgroundScheduler
realCoin = 'usd'
crypto = 'bitcoin'


url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={realCoin}'

from flask import Flask
app = Flask(__name__)

lastRate = float
pricesArray = []
def fetchCurrentRate():
    global lastRate, lastAverage, fetchCount, sum
    response = requests.get(url)
    lastRate = response.json()['bitcoin'][realCoin]
    if len(pricesArray) >= 59:
        pricesArray.pop(0)
    pricesArray.append(lastRate)


scheduler = BackgroundScheduler()
scheduler.add_job(func=fetchCurrentRate, trigger="interval", seconds=10)
scheduler.start()

@app.route("/")
def unkown():
    return "Please browse to /average or /current"

@app.route("/average")
def average():
    if len(pricesArray) < 59:
        return f"Yet to calculate the 10 minutes average. You should try again in {600-(len(pricesArray)*10)} seconds"
    else:
        return (sum(pricesArray)/len(pricesArray))


@app.route("/current")
def current():
    return str(lastRate)
