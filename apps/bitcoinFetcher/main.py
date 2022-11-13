import requests
import schedule
import time

url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur'



def job():
    sum = 0
    checkCount = 10
    for i in range(checkCount):
        response = requests.get(url)
        currentRate=response.json()['rate']
        sum += currentRate
        print (f'CurrentRate is:{currentRate}')
        time.sleep (2)
    print (f'The average is {sum/checkCount}')

# job()
# schedule.every(20).seconds.do(job)


while True:
    # schedule.run_pending()
    # time.sleep(0.1)
    job()