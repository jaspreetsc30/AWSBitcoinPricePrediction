import logging
import json

from flask import request, jsonify

from restapi import app

logger = logging.getLogger(__name__)

# make a post request with json body with key-value pair with key "name"
@app.route('/helloworld',methods=['POST'])
def helloworld():
    data = request.get_json()
    name = data.get("name")
    logging.info("My name is :{}".format(name))
    return json.dumps({"message":"Hello "+name})
