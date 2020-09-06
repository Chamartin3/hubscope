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



class CompanyViewSet(DatatablesMixin, ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    page_size = 3


    # def list(self, request, *args, **kwargs):
    #     import pdb; pdb.set_trace()
    def get_queryset(self):
        """
        """
        limited = self.request.user.groups.filter(name__in=["Gerente","Registrador"]).count() > 0
        qs = Company.objects.all()
        if limited:
            qs = qs.filter(members__person__in=[self.request.user])    
        return qs
    @action(detail=False, methods=['get'])

    
    def all(self, request, *args, **kwargs):
        qs = self.get_queryset()
        # import pdb; pdb.set_trace()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)




    @action(detail=True, methods=['get'], permission_classes=[])
    def reports(self, request, *args, **kwargs):
        '''reports'''
        company = self.get_object()
        qs = company.reports       
        serializer = ReportSerializer(qs, many=True)
        return Response(serializer.data,status=200)

    @action(detail=True, methods=['get'], permission_classes=[])
    def reportsByMetric(self, request, *args, **kwargs):
        company = self.get_object().reports
        sumary = company \
            .values('metric__name') \
            .annotate(total=Count('metric__name'))

        serializer = sumarySerializer(sumary, many=True, namefield='metric__name')
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
    def activeGoals(self, request, *args, **kwargs):
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
