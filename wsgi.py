#!/usr/bin/env python
#coding: utf-8

from __future__ import unicode_literals

import os,sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, '..'))
if PROJECT_DIR not in sys.path:
    sys.path.append(PROJECT_DIR)
tmp='/usr/local/lib/python2.7/site-packages'
if tmp not in sys.path:
    sys.path.append(tmp)
settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
if sys.getdefaultencoding() != 'utf-8':  
    reload(sys)  
    sys.setdefaultencoding('utf-8') 

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

try:
    from django.test.client import Client
    client = Client()
    client.get('/')
except Exception:
    # log error...
    pass
