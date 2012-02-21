from wsgiref.simple_server import make_server

def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!'

    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]

httpd = make_server('localhost', 8000, application)
httpd.serve_forever()
