from wsgiref.simple_server import make_server

def application(environ, start_response):
    status = '200 OK'

    output = '<html><head></head><body>'
    output += '<h1>Hello World</h1>'
    output += '</body></html>'

    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]

httpd = make_server('localhost', 8000, application)
httpd.serve_forever()
