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



class ReportViewSet(DatatablesMixin, ModelViewSet):
    queryset = Report.objects.order_by("-begin")
    serializer_class = ReportSerializer
    search_fields = ['company__id']
    filter_backends = [ reportFilters ]


    def get_queryset(self):
        """
        """
        limited = self.request.user.groups.filter(name__in=["Gerente","Registrador"]).count() > 0
        qs = Report.objects.order_by("-begin")
        if limited:
            qs = qs.filter(company__members__in=self.request.user.roles.all())    
        return qs
