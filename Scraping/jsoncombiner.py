import json
import os.path
from dateutil import parser
import requests
import datetime


response = {}
currenttime=datetime.datetime.utcnow().replace(microsecond=0)
currentiso =currenttime.isoformat()

hours_added = datetime.timedelta(hours = 2)
onehourago = currenttime - hours_added
onehouragoiso = onehourago.isoformat()



f1 = open('data1.json')
data1 = json.load(f1)
f2 = open('data2.json')
data2 = json.load(f2)

data3 = None
if os.path.exists('data3.json'):
    f3 = open('data3 copy.json')
    data3 = json.load(f3)
    print("check")

overalldata = data1 + data2
# overalldata +=response
if data3 != None:
    overalldata += data3

overalldata = [{key:row[key] for key in row  if key =="time_period_end" or key=="rate_high"} for row in overalldata]
print(overalldata[0].keys())


finaldata = {"prices":[]}
#remove duplicates
timestamps_list = []

for data in overalldata:

    data["time_period_end"] = int(parser.parse(data["time_period_end"]).timestamp() )
    if (data["time_period_end"] in timestamps_list):
        continue
    else:
        timestamps_list.append(data["time_period_end"])
        finaldata["prices"].append( list(data.values()))

print(len(finaldata["prices"]))
with open('finaldata.json', 'w', encoding='utf-8') as f:
    json.dump(finaldata, f, ensure_ascii=False, indent=4)

