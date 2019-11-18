import json
import pandas as pd


# TODO Return with JSON using jsonify. 
def request_data(x):
    """Return: JSON file"""
    json_data = [data]
    df = pd.DataFrame.from_dict(json_data, orient='columns')
    
    return df.to_json(orient='split')
