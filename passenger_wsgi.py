import sys, os
INTERP = "/usr/local/bin/python2.7"

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

import os, sys, site
site.addsitedir('/home/oskkate/rails/oskate/site-packages')
site.addsitedir('/home/oskkate/rails/oskate')
site.addsitedir('/home/oskkate/rails')
site.addsitedir('/home/oskkate/site-packages')
os.environ['LD_LIBRARY_PATH'] = '/usr/local/lib'

os.environ['DJANGO_SETTINGS_MODULE'] = 'oskate.settings'
import django.core.handlers.wsgi

from paste.exceptions.errormiddleware import ErrorMiddleware
application = django.core.handlers.wsgi.WSGIHandler()
application = ErrorMiddleware(application, debug=True)
