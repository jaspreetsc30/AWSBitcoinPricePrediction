import logging
import json
import requests 
import uuid
from flask import request,jsonify,Response
from restapi import app
import boto3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

s3Client = boto3.client(
    's3',
    aws_access_key_id="***",
    aws_secret_access_key="***",
)
s3Resource = boto3.resource(
    's3',
    aws_access_key_id="***",
    aws_secret_access_key="***",
)


def trainCoin(data):
    bitcoin_df = pd.DataFrame.from_dict(data)
    bitcoin_price_df = bitcoin_df.loc[:,"prices"]
    price_arr = bitcoin_price_df.to_numpy()
    just_price_arr = []
    just_time_stamp_arr = []
    for i in range(len(price_arr)):
        just_price_arr.append(price_arr[i][1])
        just_time_stamp_arr.append(price_arr[i][0])

    bitcoin_price_only_df = pd.DataFrame(just_price_arr)
    bitcoin_price_only_df.columns = ['Price']

    prediction_interval = 12 # meaning that 12 data points will have nan value after shifting
    bitcoin_price_only_df['Prediction'] = bitcoin_price_only_df[['Price']].shift(-prediction_interval) # prediction based off the next hour for each datapoint
    just_time_stamp_prediction_arr = just_time_stamp_arr[-prediction_interval:]
    bitcoin_price_prediction_df = bitcoin_price_only_df

    X = np.array(bitcoin_price_prediction_df.drop(['Prediction'], 1))
    X = X[: len(bitcoin_price_prediction_df)-prediction_interval] 

    y = np.array(bitcoin_price_prediction_df['Prediction'])
    y = y[: len(bitcoin_price_prediction_df)-prediction_interval]

    prediction_interval_arr = np.array(bitcoin_price_prediction_df.drop(['Prediction'],1))[-prediction_interval:] # get the original data price for the interval of prediction

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, shuffle=False) 
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma = 0.0001) # Semi Vector Machine for regression
    svr_rbf.fit(x_train,y_train)
    svr_rbf_conf = svr_rbf.score(x_test, y_test)
    interval_prediction = svr_rbf.predict(prediction_interval_arr)
    
    return (interval_prediction, just_time_stamp_prediction_arr)

#endpoint for receiving data from lamda (coin info)
@app.route('/coinRec',methods=['POST'])
def coinRec():
    data = request.get_json()
    print(data)
    new12,timeStamp = trainCoin(data)
    new12 = new12.tolist()
    print(new12, timeStamp)
    #filename as url+action+type
    predVals = {"values":new12, "timestamps":timeStamp}
    filename = "coinval.json"
    bucket_name = "comp4651"
    directory = "coinvals/"
    s3Client.put_object(Body=(bytes(json.dumps(predVals).encode('UTF-8'))), Bucket=bucket_name, Key=directory+filename)
    try:
        return json.dumps({
            'response': "Successful Uploading"
        })
    except:
        return Response("{'message':'failure'}", status=400, mimetype='application/json')


#endpoint for sending data to amplify (need to retrieve values from s3 bucket )
@app.route('/coinSend',methods=['POST'])
def coinSend():
    try:
        filename = "coinval.json"
        content_object = s3Resource.Object('comp4651', "coinvals/"+filename)
        file_content = content_object.get()['Body'].read().decode('UTF-8')
        return Response(file_content, status=200, mimetype='application/json')
    except:
        return Response("{'message':'failure'}", status=400, mimetype='application/json')
