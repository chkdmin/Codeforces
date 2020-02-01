# -*- coding: utf-8 -*-
import os

from arrow import Arrow

from codeforces import ROOT_DIR


def get_weekday(date: Arrow):
    weekday = date.weekday()
    if weekday == 0:
        return '월'
    if weekday == 1:
        return '화'
    if weekday == 2:
        return '수'
    if weekday == 3:
        return '목'
    if weekday == 4:
        return '금'
    if weekday == 5:
        return '토'
    if weekday == 6:
        return '일'

def generate_text_image(texts, margin=80):
    from PIL import Image, ImageDraw, ImageFont

    W, H = (800, 400)

    im = Image.new("RGBA", (W, H), "black")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(os.path.join(ROOT_DIR, 'BMJUA_ttf.ttf'), 45)

    for idx, text in enumerate(texts):
        w, h = draw.textsize(text, font=font)
        location = ((W - w) / 2, margin * (idx + 1))

        draw.text(location, text, font=font)

    return im
