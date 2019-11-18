from flask import Flask, render_template, request, url_for, redirect, jsonify
from .functions import get_subreddit_info


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('base.html')

    @app.route('/subreddit', methods=['POST'])
    def get_subreddits():
        subreddit_id = request.values['id']
        info = get_subreddit_info(subreddit_id)
        return render_template('subreddit.html', name=info[0], url=info[1])


    return app
