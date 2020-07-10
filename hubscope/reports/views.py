from rest_framework.viewsets import ModelViewSet
from hubscope.mixins import DatatablesMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime
from hubscope.accounts.models import User
from django.contrib.auth.models import Group

from django.db.models import Count, Sum

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

    @action(detail=True, methods=['get'], permission_classes=[])
    def reportsByMetric(self, request, *args, **kwargs):
        company = self.get_object().reports
        
        # metric = request.query_params('g')

        sumary = company \
            .values('metric__name').annotate(total=Count('metric__name'))
            # .extra(select={
            # 'metric__name':'metric__name',
            # 'name':'metric__name'
            # }) \
        # import pdb; pdb.set_trace
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



class AsignmentViewSet(DatatablesMixin, ModelViewSet):
    queryset = Asignment.objects.all()
    serializer_class = AsignmentSerializer

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
        



class IndicatorViewSet(DatatablesMixin, ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer

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

    

class ReportViewSet(DatatablesMixin, ModelViewSet):
    queryset = Report.objects.order_by("-begin")
    serializer_class = ReportSerializer
    search_fields = ['company__id']    

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

