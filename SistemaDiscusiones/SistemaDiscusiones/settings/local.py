from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'erickgarcia',
        'USER': 'erickgarcia',
        'PASSWORD': '210224942',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

#autentificacion por medio de redes sociales

SOCIAL_AUTH_FACEBOOK_KEY = '1425087194458046'
SOCIAL_AUTH_FACEBOOK_SECRET = '2a6805a10c0d241d6b761e5d1f02e2e6'

SOCIAL_AUTH_TWITTER_KEY = 'eKDLZjK2lXxyzNgAQbguV23VJ'
SOCIAL_AUTH_TWITTER_SECRET = 'syHbZqK5KEmEQlmz7VJ7nAWBA3G8EatpHamE5SzhMC8FlEwRfn'