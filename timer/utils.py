# -*- coding: utf-8 -*-
import os

from timer import ROOT_DIR


def millis_interval(diff):
    """start and end are datetime instances"""
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return millis


def generate_text_image(texts, margin=80):
    from PIL import Image, ImageDraw, ImageFont

    W, H = (800, 400)

    im = Image.new("RGBA", (W, H), "black")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(os.path.join(ROOT_DIR, 'arial.ttf'), 60)

    for idx, text in enumerate(texts):
        w, h = draw.textsize(text, font=font)
        location = ((W - w) / 2, margin * (idx + 1))

        draw.text(location, text, font=font)

    return im
