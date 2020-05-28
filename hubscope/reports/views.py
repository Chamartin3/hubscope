from rest_framework.viewsets import ModelViewSet
from hubscope.reports.serializers import CompanySerializer, AsignmentSerializer, IndicatorSerializer, ReportSerializer, CompanyRoleSerializer
from hubscope.reports.models import Company, Asignment, Indicator, Report, CompanyRole


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class AsignmentViewSet(ModelViewSet):
    queryset = Asignment.objects.all()
    serializer_class = AsignmentSerializer


class IndicatorViewSet(ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class CompanyRoleViewSet(ModelViewSet):
    queryset = CompanyRole.objects.all()
    serializer_class = CompanyRoleSerializer
