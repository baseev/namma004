import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'kisaa.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


path = 'C:/Users/Administrator/Documents/Aptana Studio 3 Workspace/namma004/'
if path not in sys.path:
    sys.path.append(path)