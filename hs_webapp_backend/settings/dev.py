from .common import *

SECRET_KEY = 'django-insecure-$us%@1mr(-q2iw9)q#*458@bsa(zzl174_*yhh+(%)h5pr0d-c'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True
