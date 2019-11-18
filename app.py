# from flask import Flask, render_template, request,  url_for, redirect, jsonify

import json
import pandas as pd


# app = Flask(__name__)
data = {
    "title": "some text",
    "self_post": "some text"
}


with open("dummy.json", "w") as reddit:
    json.dump(data, reddit)
 

# TODO Return with JSON using jsonify. 
def request_data(x):
    """Return: JSON file"""
    json_data = [data]
    df = pd.DataFrame.from_dict(json_data, orient='columns')
    
    return df.to_json(orient='split')

example = request_data(reddit)
print(example)

# if __name__ == '__main__':
#     app.run(debug=True)