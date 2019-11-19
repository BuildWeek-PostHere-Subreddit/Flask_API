from decouple import config
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, redirect, jsonify
from .functions import get_subreddit_info
import pymongo


load_dotenv()

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('base.html')

    @app.route('/subreddit', methods=['POST'])
    def get_subreddits():
        app_input = request.values['id']
        spl = app_input.split(' ')
        nums = [int(s) for s in spl]
        descriptions = get_subreddit_info(nums, config('SECRET_CODE'))
        output = []
        for description in descriptions:
            desc_dict = {}
            desc_dict['name'] = description['name']
            desc_dict['url'] = 'https://www.reddit.com' + description['url']
            desc_dict['subscribers'] = description['subscribers']
            desc_dict['active_accounts'] = description['active_accounts']
            desc_dict['score'] = description['score']
            output.append(desc_dict)

        return jsonify(output)


    return app
