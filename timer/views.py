# -*- coding: utf-8 -*-
import arrow
import requests
from flask import render_template

from . import app

link = None


@app.route('/')
def index():
    res = requests.get('https://codeforces.com/api/contest.list')
    contests = []
    for contest in res.json()['result']:
        if contest['phase'] == 'FINISHED':
            continue
        contest['date'] = arrow.get(contest['startTimeSeconds']).to('Asia/Seoul').format('YYYY-MM-DD HH:mm')
        contests.append(contest)
    contests = sorted(contests, key=lambda o: o['startTimeSeconds'])
    return render_template('index.html', contests=contests)
