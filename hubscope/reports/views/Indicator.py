
from rest_framework.viewsets import ModelViewSet
from hubscope.mixins import DatatablesMixin, datatableFilters
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
    ReportDeliverySerializer,
    Goal,
    ReportSerializer)
from hubscope.reports.models import (
    Goal,
    Metric,
    Company, 
    Asignment, 
    Indicator, 
    Position,
    Report)


class IndicatorViewSet(DatatablesMixin, ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
    


    @action(detail=False, methods=['get'])
    def all(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        # import pdb; pdb.set_trace()
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
    @action(detail=True, methods=['get'])
    def openGoals(self, request, *args, **kwargs):
        goals = self.get_object().active_goals
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data)



    @action(detail=True, methods=['get'])
    def inform(self, request, *args, **kwargs):
        '''docstring for inform'''
        indicator = self.get_object()
        begin = datetime.strptime(
            request.query_params.get('begin'),
            '%Y-%m-%d').date()
        end =  datetime.strptime(
            request.query_params.get('end'),
            '%Y-%m-%d').date()
        period = request.query_params.get('period_size')
        informe = indicator.get_informe(begin, end, period)
        serializer = InformeSerializer(informe)
        return Response(serializer.data, status=200)

class MetricViewSet(DatatablesMixin, ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    search_fields = ['name', 'desc']

    def list(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace() 
        company = request.query_params.get('company',None)
        self.queryset = self.queryset.filter(asignment__company__id__contains=company)
        return super(MetricViewSet, self).list(request, *args, **kwargs)
    
    @action(detail=False, methods=['get'], permission_classes=[])
    def all(self, request, *args, **kwargs):
        company = request.query_params.get('company',None)
        queryset = self.filter_queryset(self.get_queryset())
        if company is not None:
            queryset = queryset.filter(asignment__company__id__contains=company)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    


class GoalViewSet(ModelViewSet):
    queryset = Goal.objects.order_by("-begin")
    serializer_class = GoalSerializer
    # search_fields = ['company__id']

    
    @action(detail=True, methods=['patch'], permission_classes=[])
    def toggleStatus(self, request, *args, **kwargs):
        goal = self.get_object()
        # import pdb; pdb.set_trace()
        if goal.completed:
            goal.complete()
            txt = 'cerrado el periodo'
        else:
            goal.reopen()
            txt = 'abierto el periodo'

        return Response({'message':f'Se ha {txt} con exito'},status=200)