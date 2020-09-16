from config.base import *
import django_heroku
SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

INSTALLED_APPS = DJANGO_APPS + MODULE_APPS + MY_APPS

django_heroku.settings(locals())
