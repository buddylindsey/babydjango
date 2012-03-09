import os
from babydjango.conf import settings

class WSGIHandler():

    def __call__(self, environ, start_response):
        status = '200 OK'

        output = '<html><head></head><body>'
        output += "<h1>Hello World</h1>"
        output += '</body></html>'


        response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
        start_response(status, response_headers)

        return [output]
