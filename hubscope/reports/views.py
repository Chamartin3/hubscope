from rest_framework.viewsets import ModelViewSet
from hubscope.mixins import DatatablesMixin
from rest_framework.decorators import action
from rest_framework.response import Response

from hubscope.accounts.models import User
from django.contrib.auth.models import Group

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
    Position,
    Report)


class CompanyViewSet(DatatablesMixin, ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



    @action(detail=False, methods=['get'])
    def all(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], permission_classes=[])
    def reports(self, request, *args, **kwargs):
        '''reports'''
        company = self.get_object()
        qs = company.reports       
        serializer = ReportSerializer(qs, many=True)
        return Response(serializer.data,status=200)

    @action(detail=False,  methods=['post'], permission_classes=[])
    def manyCompaniesPersonel(self, request, *args, **kwargs):
        companies = [Company.objects.get(name=c) for c in request.data['companies']]
        groupname = request.data.pop('group')
        user = User.objects.get(id=request.data['user'])
        positions=[]
        oldroles=[oldrole.company.name for oldrole in user.roles.all() if oldrole.company.name  not in request.data['companies']]
        Position.objects.filter(company__name__in=oldroles, person=user).delete()
        for company in companies:
            obj, created = Position.objects.get_or_create(
                company = company,
                person = user,
                defaults={'name':groupname}
            )
            if not created:
                Position.objects.filter(person=obj.person).update(name=groupname)
                obj.name=groupname
            positions.append(obj)
        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data,status=200)
        

        
    def addPersonel(self, request, *args, **kwargs):
        '''reports'''
        company = self.get_object()
        groupname = request.data.pop('group')
        user = User.objects.get(id=request.data['user'])

        obj, created = Position.objects.get_or_create(
            company = company,
            person = user,
            defaults={'name':groupname}
        )
        if not created:
            Position.objects.filter(person=obj.person).update(name=groupname)
            obj.name=groupname
        group = Group.objects.get(name=groupname)
        user.groups.set([group])

        serializer = PositionSerializer(obj)
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

    def create(self, request, *args, **kwargs):
        periodicity = request.data.get('periodicity')
        if not periodicity:
            request.data['frecuency'] = 'OT'
        return super(AsignmentViewSet, self) \
            .create(request, *args, **kwargs)
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=201, headers=headers)
        



class IndicatorViewSet(DatatablesMixin, ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer

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
    

class ReportViewSet(DatatablesMixin, ModelViewSet):
    queryset = Report.objects.order_by("-begin")
    serializer_class = ReportSerializer
    search_fields = ['company__id']

