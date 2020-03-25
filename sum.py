import numpy as np 
import json

from flask import Flask, escape, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return {'message': 'Hello'}


@app.route('/summation/<json_array>', methods=['POST', 'GET'])
def compute_summation(json_array):
    return calculate_summation(json.loads(json_array))


def calculate_summation(param):
    user_list = list(param['elements'])
    sum_value = sum(user_list)
    return {'Sum': round(sum_value, 3)}


app.run()