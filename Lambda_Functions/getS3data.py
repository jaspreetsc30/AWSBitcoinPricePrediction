import json
import urllib.parse
import boto3
import requests

print('Loading function')

s3 = boto3.client('s3')
url = "http://54.210.41.176:8080/coinRec"

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        text = response["Body"].read().decode()
        data = json.loads(text)
        print(data)
        requests.post(url, json = data)
        print("DONE")
        return "Success!"
    except Exception as e:
        print(e)
        # print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e