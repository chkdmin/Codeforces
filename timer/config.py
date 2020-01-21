# -*- coding: utf-8 -*-

import os

DEBUG = True

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(ROOT_DIR, 'templates')
STATIC_DIR = os.path.join(ROOT_DIR, 'static')

# Flask-S3
FLASKS3_BUCKET_NAME = 'zappa-codeforces-contest-time-table'
FLASKS3_FILEPATH_HEADERS = {
    r'.css$': {
        'Content-Type': 'text/css',
    }
}
