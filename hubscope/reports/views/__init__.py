# from rest_framework.viewsets import ModelViewSet
# from hubscope.mixins import DatatablesMixin, datatableFilters
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from datetime import datetime
# from hubscope.accounts.models import User
# from django.contrib.auth.models import Group

# from django.db.models import Count, Sum
# from hubscope.reports.filters import reportFilters

# from hubscope.reports.serializers import AsignmentSerializer
# from hubscope.reports.models import Asignment

from .Company import CompanyViewSet
from .Reports import ReportViewSet
from .Indicator import ( IndicatorViewSet, MetricViewSet, GoalViewSet )
from .Asignment import AsignmentViewSet


# class AsignmentViewSet(DatatablesMixin, ModelViewSet):
#     queryset = Asignment.objects.all()
#     serializer_class = AsignmentSerializer

#     def list(self, request, *args, **kwargs):
#         param = request.query_params.get('company',None)
#         if param:
#             self.queryset = self.queryset.filter(company=param)
#         return super(AsignmentViewSet, self).list(self, request, *args, **kwargs)

#     def create(self, request, *args, **kwargs):
#         frecuency = request.data.get('frecuency')
#         if not frecuency:
#             request.data['frecuency'] = 'OT'
#         return super(AsignmentViewSet, self) \
#             .create(request, *args, **kwargs)



