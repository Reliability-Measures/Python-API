import numpy as np 
import json

from flask import Flask, escape, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def compute():
    # print(dict(request.args))
    name = request.args.get("json", {})
    print(name)
    return calculate_std(json.loads(name))


def calculate_std(param):
    # creates list of just values
    userList = list(param['elements'])

    # calculates STD of list of just values
    stdValue = np.std(userList)

    return {'STD': stdValue}


app.run()
