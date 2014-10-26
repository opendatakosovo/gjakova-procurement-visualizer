from flask.views import View
from flask import Response
from urllib2 import urlopen


class TreeMap(View):
    def dispatch_request(self, year):
        url = "http://0.0.0.0:5000/treemap/%d" % year
        result = urlopen(url).read()

        # Build response object.
        resp = Response(
            response=result, mimetype='application/json')

        # Return response.
        return resp