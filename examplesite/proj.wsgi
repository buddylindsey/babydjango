import os
os.environ['BABYDJANGO_SETTINGS_MODULE'] = 'examplesite.settings'

import sys
path = '/Users/percent20/Programming/Python/babydjango/'
if path not in sys.path:
    sys.path.append(path)

import babydjango.core.handlers.wsgi
application = babydjango.core.handlers.wsgi.WSGIHandler()
