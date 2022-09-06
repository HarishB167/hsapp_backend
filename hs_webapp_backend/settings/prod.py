import os
import dj_database_url
from .common import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False
ALLOWED_HOSTS = ['hsapp-backend-prod.herokuapp.com']

DATABASES = {
  'default': dj_database_url.config()
}


ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


RENDER_EXTERNAL_CORS_ORIGINS = os.environ.get('RENDER_EXTERNAL_CORS_ORIGINS')
if RENDER_EXTERNAL_CORS_ORIGINS:
    CORS_ALLOWED_ORIGINS.append(RENDER_EXTERNAL_CORS_ORIGINS)
