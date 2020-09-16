from rest_framework.viewsets import ModelViewSet
from hubscope.mixins import DatatablesMixin, datatableFilters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from datetime import datetime
from hubscope.accounts.models import User
from django.contrib.auth.models import Group
from django.db.models import Q


from django.db.models import Count, Sum
from hubscope.reports.filters import reportFilters, reportFiltersMixin

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
    ReportSerializer)
from hubscope.reports.models import (
    Goal,
    Metric,
    Company, 
    Asignment, 
    Indicator, 
    Position,
    Report)


# datatableFilters
class ReportViewSet( reportFiltersMixin, ModelViewSet):
    queryset = Report.objects.filter(metric__tipo__in=['E','A']).all()
    serializer_class = ReportSerializer
    search_fields = ['company__id']
    # filter_backends = [ reportFilters ]

    def get_object(self):
        qs=self.get_queryset()
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(qs, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj



    def get_queryset(self):
        qs = self.queryset
        limited = self.request.user \
            .groups.filter(name__in=["Gerente","Registrador"]).count() > 0
        if limited:
            qs = qs.filter(company__members__in=self.request.user.roles.all())    
        return qs
        # .filter(constant=False)


    @action(detail=True, methods=['patch'])
    def close(self, request, *args, **kwargs):
        report = self.get_object()
        result = report.close()
        if result is None:
            Response({'message': 'No Se ha podido ceerrar reporte, falta por llenar'})
        return Response({'message': 'Reporte cerrado'})

    @action(detail=True, methods=['patch'])
    def fill(self, request, *args, **kwargs):
        report = self.get_object()
        value = request.data.get('value', None)
        if value is None:
            return Response({'message': 'Valor invalido'})
        report.fill(value, request.user)
        return Response({'message': 'Reporte registrado'})



    @action(detail=False, methods=['get'])
    def allOpen(self, request, *args, **kwargs):
        qs = Report.objects.by_status('entregada')
        limited = self.request.user.groups.filter(name__in=["Gerente","Registrador"]).count() > 0
        if limited:
            qs = qs.filter(company__members__in=self.request.user.roles.all()) 
        queryset = self.filter_queryset(qs).filter(~Q(end=None))
        not_constant = self.queryset.filter(~Q(end=None))
        queryset=not_constant.intersection(queryset)
        # import pdb; pdb.set_trace()
        # queryset = queryset.filter( Q(end=None))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)


        return Response(response)




    @action(detail=False, methods=['get'])
    def allPending(self, request, *args, **kwargs):
        esperando = Report.objects.by_status('esperando')
        abierta = Report.objects.by_status('abierta')
        atrasada = Report.objects.by_status('atrasada')
        sumary = { 
            "atrasada":len(atrasada),
            "esperando":len(esperando),
            "abierta":len(abierta)
            }
        qs = atrasada | esperando | abierta
        sumary['total']=len(qs)
        
        limited = self.request.user.groups.filter(name__in=["Gerente","Registrador"]).count() > 0
        if limited:
            qs = qs.filter(company__members__in=self.request.user.roles.all()) 
    
        queryset = self.filter_queryset(qs)
        not_constant = self.queryset.filter(Q(metric__tipo__in=['A','E']) & Q(value=None) )
        queryset = queryset.intersection(not_constant)
        page = self.paginate_queryset(queryset)
        # import pdb; pdb.set_trace()
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.paginator.get_paginated_response(
                serializer.data, sumary=sumary)
        serializer = self.get_serializer(queryset, many=True)


        return Response(response)