''' Default implemetation of the vue_django aplication, recieves a list of urls (ONLY DJANGO REST FRAMEWORK API VIEWS OO MODELVIEWSET ENDPOINTS) every group of endpoints will be translated into a model in the $django.models atribute in the global Vue instance, then every option int eh endpint will be tranformed into an action that can be called as a function'''

from django.urls import path, include
from django.conf.urls import url
'''
include here your api endpoints
EXAMPLE:
url('myapp/',
include(('hubscope.urls','myapp'))
),
'''

urlpatterns = [
    url('accounts/',
        include(('hubscope.accounts.urls','accounts'))
    ),
]
