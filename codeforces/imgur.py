# -*- coding: utf-8 -*-
import base64

from imgurpython import ImgurClient as BaseImgurClient


class ImgurClient(BaseImgurClient):

    def upload_from_file(self, fd, config=None, anon=True):
        if not config:
            config = dict()

        contents = fd.read()
        b64 = base64.b64encode(contents)
        data = {
            'image': b64,
            'type': 'base64',
        }
        data.update({meta: config[meta] for meta in set(self.allowed_image_fields).intersection(config.keys())})
        fd.close()

        return self.make_request('POST', 'upload', data, anon)
