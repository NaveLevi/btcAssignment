import requests
from apscheduler.schedulers.background import BackgroundScheduler
realCoin = 'usd'
crypto = 'bitcoin'


url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={realCoin}'

from flask import Flask
app = Flask(__name__)

lastRate, lastAverage = float, float
lastAverage, fetchCount, sum = 0, 0, 0

def fetchCurrentRate():
    global lastRate, lastAverage, fetchCount, sum
    response = requests.get(url)
    lastRate = response.json()['bitcoin'][realCoin]
    sum += lastRate
    fetchCount+=1

    print (f'The average is {sum/fetchCount}')
    if (fetchCount == 60):
        lastAverage = sum / fetchCount
        sum, fetchCount = 0, 0

fetchCurrentRate() #Run first time manually

scheduler = BackgroundScheduler()
scheduler.add_job(func=fetchCurrentRate, trigger="interval", seconds=10)
scheduler.start()

@app.route("/")
def unkown():
    return "Please browse to /average or /current"

@app.route("/average")
def average():
    if (lastAverage == 0):
        return f"Yet to calculate the 10 minutes average. You should try again in {600-(fetchCount*10)} seconds"
    return str(lastAverage)

@app.route("/current")
def current():
    return str(lastRate)
