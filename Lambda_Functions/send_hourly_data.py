from dateutil import parser
import requests
import datetime
import json
import boto3

s3 = boto3.client("s3")

def lambda_handler(event, context):
    # TODO implement
    

    
    response = {}
    currenttime=datetime.datetime.utcnow().replace(microsecond=0)
    currentiso =currenttime.isoformat()
    
    hours_added = datetime.timedelta(hours = 2)
    onehourago = currenttime - hours_added
    onehouragoiso = onehourago.isoformat()
    
    # print(currentiso)
    # print(onehouragoiso)
    
    url = f"https://rest.coinapi.io/v1/exchangerate/BTC/USD/history?period_id=5MIN&time_start={onehouragoiso}Z&time_end={currentiso}"
    # url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD/history?period_id=1MIN&time_start=2016-01-01T00:00:00&time_end=2016-01-01T00:11:25"
    # print(url)
    
    headers = {'X-CoinAPI-Key' : '64E2CF0C-FA78-41ED-ADD5-7529A7F807F3'}
    response = requests.get(url, headers=headers) 
    response = json.loads(response.text)
 
    

    
    bucket =  'comp4651-rawdata'
    key = 'finaldata.json'
    
    
    data = s3.get_object(Bucket = bucket , Key= key)
    content = data["Body"]
    finaldata = json.loads(content.read())

    overalldata =  response
    
    overalldata = [{key:row[key] for key in row  if key =="time_period_end" or key=="rate_high"} for row in overalldata]
    print(overalldata[0].keys())
    
    

    #remove duplicates
    timestamps_list = []
    finaldata2 = {"prices":[]}
    for data in overalldata:
    
        data["time_period_end"] = int(parser.parse(data["time_period_end"]).timestamp() )
        if (data["time_period_end"] in timestamps_list):
            continue
        else:
            timestamps_list.append(data["time_period_end"])
            finaldata2["prices"].append( list(data.values()))


    
    
    print(finaldata2["prices"][0])

    overallfinaldata=finaldata["prices"] +finaldata2["prices"]
    finaldata2 = {"prices":[]}
    timestamps_list = []

    for data in overallfinaldata:
        
        if (data[0] in timestamps_list):
            continue
        else:
            timestamps_list.append(data[0])
            finaldata2["prices"].append(data)    

    
    
    


    
    uploadByteStream = bytes(json.dumps(finaldata2).encode("UTF-8"))
    s3.put_object(Bucket=bucket, Key="finaldata.json" , Body=uploadByteStream)
    print("Done")
    
    
    return
