"""HubScope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from hubscope.navigation import Home
from hubscope.api import urlpatterns as api
# TODO:add this as a template tag
from .vue_django.views import VueDjangoConfig, ServiceWorker

urlpatterns = [
    url('api/', include((api, "api"), namespace='api')),
    path('vue_django/', VueDjangoConfig.as_view(), name="vue_django"),
    path('service_worker/', ServiceWorker.as_view(), name="service_worker"),
    path('admin/', admin.site.urls),
    url('', Home.as_view(), name='home'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
