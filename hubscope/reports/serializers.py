from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from hubscope.reports.models import (
    Position, 
    Metric, 
    Company, 
    Asignment, 
    Indicator,
    Goal, 
    Report)
from hubscope.accounts.models import User


class sumarySerializer(Serializer):
    total = serializers.IntegerField()
    def __init__(self, *args, **kwargs):
        namefield=kwargs.pop('namefield', None)
        if namefield is not None:
            self.fields['name'] =  serializers.CharField(source=namefield)
        return super(sumarySerializer,self).__init__(*args, **kwargs)


class GoalStatusSerializer(ModelSerializer):
    indicatorname = serializers.SerializerMethodField()
    def get_indicatorname(self, goal):
        # import pdb; pdb.set_trace()
        return goal.indicator.name
    class Meta:
        model = Goal
        fields = [
            'id',
            'period',
            'indicatorname',
            'status',
        ]



class GoalSerializer(ModelSerializer):
    indicatorname = serializers.SerializerMethodField()
    result = serializers.SerializerMethodField()

    def get_indicatorname(self, goal):
        return goal.indicator.name

    def get_result(self, goal):
        if goal.completed:
            return goal.result
        else:
            return goal.computed_result

    class Meta:
        model = Goal
        fields = [
            'id',
            'group',
            'begin',
            'end',
            'fail',
            'goal',
            'indicator',

            'indicatorname',
            'report_rate',
            'completed',
            'duration',
            'period',
            'chart',
            'acomplishment',
            'status',
            'expected',
            'result',
            ]
        read_only_fields = [
            'id',
            'indicatorname',
            'report_rate',
            'completed',
            'duration',
            'period',
            'chart',
            'acomplishment',
            'status',
            'expected',
            'result'
            ]


class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','fullname','last_login']    

class MetricSerializer(ModelSerializer):
    class Meta:
        model = Metric
        fields = ['id','name', 'tipo', 'unidad', 'desc']


class PositionSerializer(ModelSerializer):
    user = serializers.SerializerMethodField()
    company = serializers.StringRelatedField()
    class Meta:
        model = Position
        fields =  ['user','name','company']

    def get_user(self, position):
        user= position.person
        # import pdb; pdb.set_trace()
        return {
            "id":user.id,
            "username":user.username,
            "fullname":user.fullname,
            "ultimo_login":user.last_login
        }




class IndicatorSerializer(ModelSerializer):
    recent_goals = GoalSerializer(many=True)
    # periods = GoalSerializer(many=True)
    # active_periods = GoalSerializer(many=True)
    class Meta:
        model = Indicator
        fields = [
            'id',
            'name',
            'unidad',
            'desc',
            'tipo',
            'active',
            'metrics',
            'company',
            'recent_goals'       
        ]

        
class ReportSerializer(ModelSerializer):
    name = serializers.SerializerMethodField()
    unidad = serializers.SerializerMethodField()
    registered_by = UserInfoSerializer(read_only=True)
    modified_by = UserInfoSerializer(read_only=True)
    metric = MetricSerializer()
    editable = serializers.BooleanField(required=False)
    class Meta:
        model = Report
        fields = [
            'id',
            'metric',
            'name',
            'value',
            'begin',
            'end',
            'days',
            'status',
            'delay',
            'delayed',
            'deadline',
            'editable',
            'unidad',
            'created_at',
            'registered_by',
            'updated_at',
            'modified_by']

    def get_valor(self, report):
        return report.value    

    def get_name(self, report):
        return report.metric.name

    def get_unidad(self, report):
        return report.metric.unidad
    # def val(self, report):
    #     return report['value']


class CompanySerializer(ModelSerializer):
    # expected_reports = AsignmentSerializer(many=True)
    reports = ReportSerializer(many=True)
    open_goals = GoalStatusSerializer(many=True)
    # indicators = IndicatorSerializer(many=True) 
    class Meta:
        model = Company
        fields = [
            'id',
            'name', 
            'reports', 
            'open_goals'
            # 'indicators', 
            # 'expected_reports'
            ]
class AsignmentSerializer(ModelSerializer):
    next_ocurrence = serializers.DateField(required=False)
    deadline_date = serializers.DateField(read_only=True)
    active_goal = ReportSerializer(read_only=True)
    metric_info = MetricSerializer(read_only=True, source="metric")

    class Meta:
        model = Asignment
        fields =  [
            'metric',
            'metric_info',
            'company',
            'last',
            'metafreq',
            'delivery_time',
            'frecuency',
            'days',
            'active_goal',
            'next_ocurrence',
            'deadline_date'
        ]

class DayResultField(serializers.DictField):
    date = serializers.CharField()
    value = serializers.DecimalField(max_digits=6, decimal_places=2)

# class IndicatorResultsField(serializers.ListField):
    

class InformeSerializer(Serializer):
    begin = serializers.DateField(read_only=True)
    end = serializers.DateField(read_only=True)
    total_mising = serializers.IntegerField()
    delivery_rate = serializers.DecimalField(max_digits=6, decimal_places=2)
    mising = serializers.ListField(
        child=serializers.DateField()
    )    
    total_overlaped = serializers.IntegerField()
    overlaped = serializers.ListField(
        child=serializers.DateField()
    )
    total_reports = serializers.IntegerField()
    period_size = serializers.IntegerField()


    val_agregated = serializers.IntegerField()
    val_in_periods = serializers.ListField(
        child = DayResultField()
    )


    reported_days = serializers.IntegerField()
    days_to_report = serializers.IntegerField()
    def create(self, validated_data):
        return "Not mplemented"
        
    def update(self, instance, validated_data):
        return "Not mplemented"
