#!/usr/bin/env python3
""" flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)


class Config(object):
    """ Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello():
    """ render html file """
    return render_template('0-index.html')


@babel.localeselector
def get_locale():
    """ best match with the supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
