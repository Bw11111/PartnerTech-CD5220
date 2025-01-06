import requests
import sys
import serial
import json
import time
def getPrice():
    symbol = 'AAPL'
    api_url = 'https://api.api-ninjas.com/v1/stockprice?ticker={}'.format(symbol)
    response = requests.get(api_url, headers={'X-Api-Key': 'CnHd9c4mIiMB4/Zfyy39+Q==EGOTl8GsZk0ntPJP'})
    if response.status_code == requests.codes.ok:
        return json.loads(response.text)['price']
    
    else:
        print("Error:", response.status_code, response.text)
serialPort = serial.Serial(
    port="COM3", baudrate=9600, bytesize=8, timeout=0, stopbits=serial.STOPBITS_ONE
)

t=600
while True:
    if t >= 600:
        serialPort.write(b"!#9" + str(getPrice()).encode())
        t=0
    else:
        t+=1
        time.sleep(1)