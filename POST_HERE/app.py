from decouple import config
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, redirect, jsonify
from .functions import get_subreddit_info
from .models import Post_Model, Username_Model
import numpy as np
import pymongo
import random


load_dotenv()

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('base.html')

    @app.route('/subreddit', methods=['GET'])
    def get_subreddits():
        model = Post_Model()
        prediction = model.predict()
        subreddits = get_subreddit_info(prediction, config('SECRET_CODE'))
        output = []
        for subreddit in subreddits:
            sub_dict = {}
            sub_dict['name'] = subreddit['name']
            sub_dict['url'] = 'https://www.reddit.com' + subreddit['url']
            sub_dict['subscribers'] = subreddit['subscribers']
            sub_dict['active_accounts'] = subreddit['active_accounts']
            sub_dict['score'] = subreddit['score']
            if type(subreddit['description']) is float:
                sub_dict['description'] = 'None'
            else:
                sub_dict['description'] = subreddit['description']
            output.append(sub_dict)

        return jsonify(output)

    @app.route('/username', methods=['POST'])
    def from_username(name=None):
        name = name or request.values['user_name']




    return app
