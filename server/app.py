#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count_parameter(parameter):
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
