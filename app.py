from flask import Flask, render_template, request,  url_for, redirect, jsonify


app = Flask(__name__)

def request_data():
    """Gets data in JSON format and runs it through the model.
       :return: JSON file.
    """
    reddit = request.get_json()

    # Non-default values. Needs to have user input or breaks the app.
    # TODO variables for title and self_post
    title = reddit['title'] # Example
    self_post = reddit['self_post'] # Example
    # TODO Combine into a single text. 

    # No defaulted values. 

    features = {'title': title, 'self_post': self_post}

    # Converts the data into a DataFrame object.
    predict_data = pd.DataFrame(features, index=[1])

    # Using pickle file with encode/categorize the data. 
    # TODO Needs to be changed to corrected variables and pickle object name. 
    features_encoder = encoder.transform(predict_data) 

    # Feeds the data into the model.
    # TODO Needs to be 
    prediction = model.predict(features_encoder)

    # Returns prediction in a JSON format and within, a float.
    return jsonify({'prediction': prediction[0]}) # TODO LIST OF SUBREDDITS


if __name__ == '__main__':
    app.run(debug=True)