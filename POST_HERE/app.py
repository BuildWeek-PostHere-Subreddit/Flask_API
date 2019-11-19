from decouple import config
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify
from .functions import get_subreddit_info
import random

load_dotenv()


def create_app():
    app = Flask(__name__)

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

        return jsonify(output)

    return app
