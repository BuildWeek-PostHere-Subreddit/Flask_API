from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_cors import CORS
from .functions import jsonConversion, list_subreddits
from .models import Post_Model, Username_Model
import pymongo


load_dotenv()


def create_app():
    app = Flask(__name__)
    CORS(app)
    # Allow CORS from the above domain on all routes

    @app.route('/')
    def index():
        return render_template('base.html')

    @app.route('/subreddit', methods=['POST'])
    def get_subreddits():
        submission = request.get_json(force=True)
        model_input = jsonConversion(submission)
        model = Post_Model()
        prediction = model.predict(model_input)
        output = list_subreddits(prediction)

        return jsonify(output)  

    @app.route('/subreddit_test', methods=['POST'])
    def get_subreddits_test():
        title, text, link = sorted([request.values['title'],
                                    request.values['text'],
                                    request.values['link']])
        submission = {"title": title, "text": text, "link": link}
        model_input = jsonConversion(submission)
        model = Post_Model()
        prediction = model.predict(model_input)
        output = list_subreddits(prediction)

        return jsonify(output)

    @app.route('/username', methods=['POST'])
    def from_username(name=None):
        name = name or request.values['user_name']
        model = Username_Model(name=name)
        prediction = model.predict()
        output = list_subreddits(prediction)

        return jsonify(output)

    return app
