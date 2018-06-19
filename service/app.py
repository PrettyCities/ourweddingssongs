import falcon
from service.twilio_intercepter import TwilioIntercepter

api = application = falcon.API()

api.req_options.auto_parse_form_urlencoded = True
twilio_intercepter = TwilioIntercepter()

application.add_route('/message', twilio_intercepter)
