from decouple import config
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, redirect, jsonify
from .functions import get_subreddit_info
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
        rand_nums = [random.randint(1,1000) for _ in range(10)]
        descriptions = get_subreddit_info(rand_nums, config('SECRET_CODE'))
        output = []
        for description in descriptions:
            desc_dict = {}
            desc_dict['name'] = description['name']
            desc_dict['url'] = 'https://www.reddit.com' + description['url']
            desc_dict['description'] = description['description']
            desc_dict['subscribers'] = description['subscribers']
            desc_dict['active_accounts'] = description['active_accounts']
            desc_dict['score'] = description['score']
            output.append(desc_dict)

        return jsonify(output)


    return app
