from . import *

SECRET_KEY = '-~aO;| F;rE[??/w^zcumh(9'
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME': 'disquaire2', # le nom de notre base de données créée précédemment
        'USER': 'mathieu92250', # attention : remplacez par votre nom d'utilisateur !!
        'PASSWORD': 'borisfdp92',
        'HOST': '',
        'PORT': '5432',
    }
}

