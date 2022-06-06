import requests
import json
import datetime

currenttime=datetime.datetime.utcnow().replace(microsecond=0)
currentiso =currenttime.isoformat()

url1 = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD/history?period_id=5MIN&time_start=2021-09-06T00:00:00.0000000Z&time_end=2021-10-06T00:00:00&limit=10000'
url2 = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD/history?period_id=5MIN&time_start=2021-10-06T00:00:00.0000000Z&time_end=2021-11-06T00:00:00&limit=10000'
url3 = f"https://rest.coinapi.io/v1/exchangerate/BTC/USD/history?period_id=5MIN&time_start=2021-11-06T00:00:00.0000000Z&time_end={currentiso}&limit=10000"

headers = {'X-CoinAPI-Key' : '***************'}
response = requests.get(url1, headers=headers) 
response = json.loads(response.text)
with open('data1.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, ensure_ascii=False, indent=4)

response = requests.get(url2, headers=headers) 
response = json.loads(response.text)
with open('data2.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, ensure_ascii=False, indent=4)

response = requests.get(url3, headers=headers) 
response = json.loads(response.text)
with open('data3.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, ensure_ascii=False, indent=4)