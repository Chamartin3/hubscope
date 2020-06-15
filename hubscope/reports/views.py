from rest_framework.viewsets import ModelViewSet
from hubscope.mixins import DatatablesMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from hubscope.reports.serializers import (
    CompanySerializer, 
    AsignmentSerializer, 
    IndicatorSerializer, 
    PositionSerializer,
    MetricSerializer,
    ReportSerializer)
from hubscope.reports.models import (
    Metric,
    Company, 
    Asignment, 
    Indicator, 
    Report)


class CompanyViewSet(DatatablesMixin, ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'], permission_classes=[])
    def reports(self, request, *args, **kwargs):
        '''reports'''
        company = self.get_object()
        qs = company.reports       
        serializer = ReportSerializer(qs, many=True)
        return Response(serializer.data,status=200)


    @action(detail=True, methods=['get'], permission_classes=[])
    def personel(self, request, *args, **kwargs):
        '''asociated persons'''
        company = self.get_object()
        qs = company.members       
        serializer = PositionSerializer(qs, many=True)
        return Response(serializer.data,status=200)


    @action(detail=True, methods=['get'], permission_classes=[])
    def acomplishments(self, request, *args, **kwargs):
        company = self.get_object()
        qs = company.reports
        

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, 
            status=201, 
            headers=headers)       
    

class AsignmentViewSet(DatatablesMixin, ModelViewSet):
    queryset = Asignment.objects.all()
    serializer_class = AsignmentSerializer


class IndicatorViewSet(DatatablesMixin, ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer

class MetricViewSet(DatatablesMixin, ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        # import pdb; pdb.set_trace()
        return serializer_class(*args, **kwargs)

class ReportViewSet(DatatablesMixin, ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    search_fields = ['company__id']

