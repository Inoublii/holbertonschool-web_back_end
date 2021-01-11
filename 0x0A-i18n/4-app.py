#!/usr/bin/env python3
""" flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
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
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ best match with the supported languages """
    if request.args.get('locale'):
        x = request.args.get('locale')
        if x in app.config['LANGUAGES']:
            return x
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':

    app.run()
