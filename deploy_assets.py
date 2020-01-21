# -*- coding: utf-8 -*-

import flask_s3

from timer import app

flask_s3.create_all(app)
