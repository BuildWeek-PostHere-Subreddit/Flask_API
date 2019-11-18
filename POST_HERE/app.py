from flask import Flask, render_template, request,  url_for, redirect, jsonify


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello world!'

    return app
