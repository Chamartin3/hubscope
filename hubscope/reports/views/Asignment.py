from rest_framework.viewsets import ModelViewSet
from hubscope.mixins import DatatablesMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime
from hubscope.accounts.models import User
from django.contrib.auth.models import Group

from django.db.models import Count, Sum
from hubscope.reports.filters import reportFilters

from hubscope.reports.serializers import (
    GoalSerializer, 
    CompanySerializer, 
    AsignmentSerializer, 
    IndicatorSerializer, 
    PositionSerializer,
    InformeSerializer,
    MetricSerializer,
    sumarySerializer,
    ReportSerializer)
from hubscope.reports.models import (
    Goal,
    Metric,
    Company, 
    Asignment, 
    Indicator, 
    Position,
    Report)


class AsignmentViewSet(DatatablesMixin, ModelViewSet):
    queryset = Asignment.objects.all()
    serializer_class = AsignmentSerializer

    def list(self, request, *args, **kwargs):
        param = request.query_params.get('company',None)
        if param:
            self.queryset = self.queryset.filter(company=param)
        return super(AsignmentViewSet, self).list(self, request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        frecuency = request.data.get('frecuency')
        if not frecuency:
            request.data['frecuency'] = 'OT'
        return super(AsignmentViewSet, self) \
            .create(request, *args, **kwargs)
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=201, headers=headers)
        

