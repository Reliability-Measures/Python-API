import numpy as np 
import json

from flask import Flask, escape, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return {'message': 'Hello'}


@app.route('/std/<json_array>', methods=['POST', 'GET'])
def compute_std(json_array):
    return calculate_std(json.loads(json_array))


def calculate_std(param):
    user_list = list(param['elements'])
    std_value = np.std(user_list)
    return {'Std': round(std_value, 3)}


app.run()