from dotenv import load_dotenv

from .functions import get_subreddit_info

from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_cors import CORS
from .functions import list_subreddits
from .models import Post_Model, Username_Model
import pymongo

import random

load_dotenv()


def create_app():
    app = Flask(__name__)
    CORS(app) # Allow CORS for all domains on all routes

    @app.route('/')
    def index():
        return render_template('base.html')

    @app.route('/subreddit', methods=['GET'])
    def get_subreddits():
        rand_nums = [random.randint(1, 1000) for _ in range(10)]
        descriptions = get_subreddit_info(rand_nums, config('SECRET_CODE'))
        output = []
        for description in descriptions:
            desc_dict = {'name': description['name'], 'url': 'https://www.reddit.com' + description['url'],
                         'subscribers': description['subscribers'], 'active_accounts': description['active_accounts'],
                         'score': description['score']}
            output.append(desc_dict)
            
        model = Post_Model()
        prediction = model.predict()
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
