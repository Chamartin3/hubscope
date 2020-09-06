from rest_framework.viewsets import ModelViewSet
from hubscope.mixins import DatatablesMixin, datatableFilters
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime
from hubscope.accounts.models import User
from django.contrib.auth.models import Group

from django.db.models import Count, Sum
from hubscope.reports.filters import reportFilters

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
    

    @action(detail=True, methods=['patch'])
    def fill(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ReportDeliverySerializer(
            instance, 
            data=request.data, 
            partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


    @action(detail=False, methods=['get'])
    def allOpen(self, request, *args, **kwargs):
        qs = Report.objects.by_status('entregada')
        limited = self.request.user.groups.filter(name__in=["Gerente","Registrador"]).count() > 0
        if limited:
            qs = qs.filter(company__members__in=self.request.user.roles.all()) 
        queryset = self.filter_queryset(qs)
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
        page = self.paginate_queryset(queryset)
        # import pdb; pdb.set_trace()
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.paginator.get_paginated_response(
                serializer.data, sumary=sumary)
        serializer = self.get_serializer(queryset, many=True)


        return Response(response)
        