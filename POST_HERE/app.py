from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, redirect, jsonify
from .functions import list_subreddits
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
