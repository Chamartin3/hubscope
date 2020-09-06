
from rest_framework.serializers import ModelSerializer, Serializer, SerializerMethodField
from rest_framework import serializers
from hubscope.reports.models import (
    Position, 
    Metric, 
    Company, 
    Asignment, 
    Indicator,
    Goal, 
    Report)



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

