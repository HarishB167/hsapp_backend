import os
import dj_database_url
from .common import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False
ALLOWED_HOSTS = ['hsapp-backend-prod.herokuapp.com']

DATABASES = {
  'default': dj_database_url.config()
}

if os.environ.get('MYSQL_ATTR_SSL_CA'):
    DATABASES['default']['OPTIONS'] = {'ssl': {'ca': os.environ.get('MYSQL_ATTR_SSL_CA')}}


ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


RENDER_EXTERNAL_CORS_ORIGINS = os.environ.get('RENDER_EXTERNAL_CORS_ORIGINS')
if RENDER_EXTERNAL_CORS_ORIGINS:
    origins = RENDER_EXTERNAL_CORS_ORIGINS.split(',')
    CORS_ALLOWED_ORIGINS += origins
