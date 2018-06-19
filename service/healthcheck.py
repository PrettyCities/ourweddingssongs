from falcon import MEDIA_TEXT
from falcon.response import Response
from falcon.request import Request


class HealthCheck(object):
    def on_get(self, req: Request, res: Response):
        res.body = "All good!"
        res.content_type = MEDIA_TEXT
