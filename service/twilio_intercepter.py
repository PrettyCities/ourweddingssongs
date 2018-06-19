import os

import falcon
from falcon.response import Response
from falcon.request import Request
from falcon import MEDIA_XML
from twilio.rest import Client

from ows_settings import TWILIO_AUTH_TOKEN
from ows_settings import TWILIO_ACCOUNT_SID
from ows_settings import TWILIO_FROM_NUMBER
from service.models.twilio_message import TwilioMessage
from websitemaker.utils.spotify_song_finder import SpotifySongFinder
from websitemaker.aws_services import AwsServices


class TwilioIntercepter(object):
    def on_post(self, req: Request, res: Response):
        twilio_message = TwilioMessage.apply(req.params)
        if twilio_message.is_song_request:
            song_request = twilio_message.extract_song()

            spotify_uri = SpotifySongFinder.lucky_find(artist=song_request.artist,
                                                       track=song_request.title)

            song_request.uri = spotify_uri

            AwsServices.add(**song_request.to_kwargs())
            self.twilio_reply(to=twilio_message.msg_from)

            res.status = falcon.HTTP_CREATED
        else:
            res.status = falcon.HTTP_BAD_REQUEST

        res.content_type = MEDIA_XML
        res.body = '<?xml version=\"1.0\" encoding=\"UTF-8\"?>' \
                   '<Response></Response>'

    def twilio_reply(self, to):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            to=to,
            from_=TWILIO_FROM_NUMBER,
            body="Your song has been added!"
        )
