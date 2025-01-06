import os
import requests
import json
import time
def getPrice():
    symbol = 'AAPL'
    api_url = 'https://api.api-ninjas.com/v1/stockprice?ticker={}'.format(symbol)
    response = requests.get(api_url, headers={'X-Api-Key': 'key'})
    if response.status_code == requests.codes.ok:
        return json.loads(response.text)['price']
    
    else:
        print("Error:", response.status_code, response.text)
t=595
while True:
    if t >= 600:
        os.system("C:\\Users\\Minec\\source\\repos\\SendData\\x64\\Debug\\SendData.exe COM3 " + "1StonkMaster 5000")
        os.system("C:\\Users\\Minec\\source\\repos\\SendData\\x64\\Debug\\SendData.exe COM3 " + "2AAPL: $"+str(getPrice()))
        t=0
    else:
        t+=1
        print(t)
        time.sleep(1)
