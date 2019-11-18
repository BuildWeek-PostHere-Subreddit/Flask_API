from flask import Flask, render_template, request,  url_for, redirect, jsonify


app = Flask(__name__)

@app.route('/')
def index():

    return pass


if __name__ == '__main__':
    app.run(debug=True)
