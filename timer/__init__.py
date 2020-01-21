# -*- coding: utf-8 -*-
import os
from configparser import ConfigParser

from flask import Flask
from flask_s3 import FlaskS3

from timer.config import ROOT_DIR, TEMPLATE_DIR, STATIC_DIR
from timer.imgur import ImgurClient

imgur_client = None


def init_config(app_):
    from timer import config
    for c in dir(config):
        if c.startswith('__') and c.endswith('__'):
            continue
        attr = getattr(config, c, None)
        if attr is None:
            continue

        app_.config[c] = attr


def init_flask_s3(app_):
    with open(os.path.join(ROOT_DIR, '.aws/credentials')) as f:
        config = ConfigParser()
        config.read_file(f)

    app_.config['AWS_ACCESS_KEY_ID'] = config['zappa-personal']['aws_access_key_id']
    app_.config['AWS_SECRET_ACCESS_KEY'] = config['zappa-personal']['aws_secret_access_key']

    FlaskS3(app_)


def init_imgur_client():
    global imgur_client
    with open(os.path.join(ROOT_DIR, '.imgur/credentials')) as f:
        config = ConfigParser()
        config.read_file(f)

    imgur_client = ImgurClient(client_id=config['default']['client_id'],
                               client_secret=config['default']['client_secret'])


def create_app():
    app_ = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
    init_config(app_)
    init_flask_s3(app_)
    init_imgur_client()
    return app_


app = create_app()
import timer.views
