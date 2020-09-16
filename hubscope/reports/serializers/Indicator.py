
from rest_framework.serializers import ModelSerializer, Serializer, SerializerMethodField
from rest_framework import serializers
from hubscope.reports.models import (
    Metric,
    Indicator,
    Goal,
    Components)



class MetricSerializer(ModelSerializer):
    value = serializers.IntegerField(write_only=True, required=False)
    has_indicators = SerializerMethodField()
    constant_value = SerializerMethodField()
    class Meta:
        model = Metric
        fields = ['id','name', 'tipo', 'unidad', 'desc','value', 'has_indicators', 'constant_value']
    
    def get_has_indicators(self, metric):
        return metric.indicators.count()
    
    def get_constant_value(self, metric):
        if metric.tipo == 'C':
            return metric.value_of_constant
        return None

    def validate(self, data):
        """
        Check that start is before finish.
        """
        value=data.get('value', None)
        tipo=data.get('tipo')
        if tipo=='C' and value is None:
            raise serializers.ValidationError({"value":"Cuando se crea una constante es necesario agregar un valor"})
        return data
    

    #  def create(self, validated_data):
    #     value = validated_data.get('value', None)
    #     tipo = validated_data.get('tipo', None)
    #     if tipo === 'C' and value is None:

    #     indicator = Indicator.objects.create(**validated_data)
    #     for comp_data in components:
    #         Components.objects.create(indicator=indicator, **comp_data)
    #     return indicator

class GoalStatusSerializer(ModelSerializer):
    indicatorname = SerializerMethodField()
    def get_indicatorname(self, goal):
        # import pdb; pdb.set_trace()
        return goal.indicator.name    
    class Meta:
        model = Goal
        fields = [
            'id',
            'name',
            'period',
            'indicatorname',
            'status',
        ]

class MiniGoalSerializer(ModelSerializer):
    indicatorname = SerializerMethodField()
    company_name = SerializerMethodField()
    class Meta:
        model = Goal
        fields = [
            'id',
            'name',
            'status',
            'begin',
            'end',
            'indicatorname',
            'variance_chart',
            'acomplishment',
            'company_name'
        ]
        

    def get_company_name(self, goal):
        if goal.indicator.company:
            return goal.indicator.company.name
        return ''

    def get_indicatorname(self, goal):
        return goal.indicator.name

class GoalSerializer(ModelSerializer):
    indicatorname = SerializerMethodField()
    result = SerializerMethodField()

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
            'name',
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



class ComponentsSerializer(ModelSerializer):
    metric_name = SerializerMethodField()
    class Meta:
        model = Components
        fields = [
            'metric_name',
            'metrica',
            'role'
        ]


    def get_metric_name(self, component):
        if component.metrica:
            return component.metrica.name
        return ''

class IndicatorSerializer(ModelSerializer):
    company_name = SerializerMethodField()
    components = ComponentsSerializer(many=True)
    metrics = MetricSerializer(many=True, read_only=True)
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
            'company_name',
            'total_active_goals',
            'components',
            # 'metrics',
            # 'recent_goals'       
        ]

    def get_company_name(self,indicator):
        if indicator.company:
            return indicator.company.name
        return ''

    def create(self, validated_data):
        components = validated_data.pop('components')
        indicator = Indicator.objects.create(**validated_data)
        for comp_data in components:
            Components.objects.create(indicator=indicator, **comp_data)
        return indicator


class DayResultField(serializers.DictField):
    date = serializers.CharField()
    value = serializers.DecimalField(max_digits=6, decimal_places=2)

class InformeSerializer(Serializer):
    begin = serializers.DateField(read_only=True)
    end = serializers.DateField(read_only=True)
    total_mising = serializers.IntegerField()
    missing = serializers.ListField(
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
    total_days_to_report = serializers.IntegerField()
    delivery_rate = serializers.DecimalField(max_digits=6, decimal_places=2)
    def create(self, validated_data):
        return "Not mplemented"
        
    def update(self, instance, validated_data):
        return "Not mplemented"