from django.conf import settings
from importlib import import_module
from django.views.generic import TemplateView
# from django.utils.html import mark_safe
from django.middleware.csrf import get_token
from .utils import get_auth_user, get_authentication, get_routes, APIMap

import json
from django.utils.html import mark_safe

api= import_module(getattr(settings, "DJV_API_URLS", None ))

class ServiceWorker(TemplateView):
    template_name="sw.js"


class VueDjangoConfig(TemplateView):
    template_name="vue_django.js"

    def get_context_data(self, **kwargs):
        map = APIMap(api)

        context = {
            'user':get_auth_user(self.request),
            'csrf_token': get_token(self.request),
            'autentication':get_authentication(),
            '_actions':map.modelMap,
            **get_routes(api)
            }

        # con = mark_safe(json.dumps(context))
        return {'vue_django_vars':mark_safe(json.dumps(context))}
