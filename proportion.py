import numpy as np 
import json

from flask import Flask, escape, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return {'message': 'Hello'}


@app.route('/proportion/<json_array>', methods=['POST', 'GET'])
def compute_proportion(json_array):
    return calculate_proportion(json.loads(json_array))


def calculate_proportion(param):
    user_list = list(param['twoElements'])
    propo_value = np.divide(user_list[0], user_list[1])
    return {'Proportion': round(propo_value, 3)}


app.run()