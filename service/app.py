import falcon
from service.healthcheck import HealthCheck
from service.twilio_intercepter import TwilioIntercepter

api = application = falcon.API()

api.req_options.auto_parse_form_urlencoded = True

health_check = HealthCheck()
twilio_intercepter = TwilioIntercepter()

application.add_route('/message', twilio_intercepter)
application.add_route('/healthcheck', health_check)
