from rest_framework.serializers import ModelSerializer
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

class GoalSerializer(ModelSerializer):
    class Meta:
        model = Goal
        fields = [
            'group',
            'begin',
            'end',
            'fail',
            'goal',
            'duration',
            'calculated_results',
            'completed',
            'period',
            ]


class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','fullname','last_login']    

class MetricSerializer(ModelSerializer):
    class Meta:
        model = Metric
        fields = ['name', 'tipo', 'unidad', 'desc']


class PositionSerializer(ModelSerializer):
    user = serializers.SerializerMethodField()
    company = serializers.StringRelatedField()
    class Meta:
        model = Asignment
        fields =  ['user','name','company']

    def get_user(self, position):
        user= position.person
        return {
            "username":user.username,
            "fullname":user.fullname,
            "ultimo_login":user.last_login
        }

class AsignmentSerializer(ModelSerializer):
    class Meta:
        model = Asignment
        fields =  [
            'metric',
            'company',
            'last',
            'frecuency',
        ]

class IndicatorSerializer(ModelSerializer):
    recent_periods = GoalSerializer(many=True)
    # periods = GoalSerializer(many=True)
    # active_periods = GoalSerializer(many=True)
    class Meta:
        model = Indicator
        fields = [
            'name',
            'unidad',
            'desc',
            'tipo',
            'active',
            'metrics',
            'company',
            # 'active_periods',
            # 'completed_periods',
            'recent_periods',       
            # 'periods',       
        ]

        
class ReportSerializer(ModelSerializer):
    name = serializers.SerializerMethodField()
    unidad = serializers.SerializerMethodField()
    registered_by = UserInfoSerializer()
    metric = MetricSerializer()
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
    # indicators = IndicatorSerializer(many=True) 
    class Meta:
        model = Company
        fields = [
            'id',
            'name', 
            'reports', 
            # 'indicators', 
            # 'expected_reports'
            ]