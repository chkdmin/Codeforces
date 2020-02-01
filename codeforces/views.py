# -*- coding: utf-8 -*-
from io import BytesIO

import arrow
import requests
from flask import render_template

from codeforces.utils import generate_text_image, get_weekday
from . import app, imgur_client

result = None
link = None


@app.route('/')
def index():
    global result
    if result is None:
        result = requests.get('https://codeforces.com/api/contest.list').json()['result']

    contests = []
    for contest in result:
        if contest['phase'] == 'FINISHED':
            continue
        d = arrow.get(contest['startTimeSeconds']).to('Asia/Seoul')
        contest['date'] = d.format('YYYY-MM-DD HH:mm')
        contest['display_date'] = d.format(f'MM월 DD일({get_weekday(d)}) HH시 mm분')
        contests.append(contest)
    contests = sorted(contests, key=lambda o: o['startTimeSeconds'])

    # 곧 시작하는 대회 체크
    next_contests = []
    upcoming_contests = []
    next_contest = contests[0]
    for contest in contests:
        if contest['startTimeSeconds'] == next_contest['startTimeSeconds']:
            next_contests.append(contest)
        else:
            upcoming_contests.append(contest)

    # Before 구하기
    seconds = abs(next_contest['relativeTimeSeconds'])
    days = seconds // 3600 // 24
    seconds -= (days * 24 * 3600)
    hours = seconds // 3600
    seconds -= (hours * 3600)
    minutes = seconds // 60
    seconds -= (minutes * 60)
    before = ''
    if days >= 1:
        before += f'{days} day '
    before += '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

    global link
    if link is None:
        # 미리보기 이미지 생성 및 업로드
        im = generate_text_image((
            next_contest['name'],
            f'{contest["display_date"]}',
            f'{before}'
        ))
        output = BytesIO()
        im.save(output, format="png")
        output.seek(0)

        im = imgur_client.upload_from_file(output)
        link = im['link']

    return render_template('index.html',
                           image_link=link,
                           next_contests=next_contests,
                           upcoming_contests=upcoming_contests)
