from rest_framework.serializers import ModelSerializer, Serializer, SerializerMethodField
from rest_framework import serializers

from .Indicator import  (
    GoalSerializer,
    IndicatorSerializer,
    GoalStatusSerializer,
    InformeSerializer,
    MiniGoalSerializer
)

from .Reports import (
    ReportSerializer,
    MetricSerializer,
    ReportDeliverySerializer
)

from .Company import CompanySerializer, PositionSerializer

from .Asignment import AsignmentSerializer


class sumarySerializer(Serializer):
    total = serializers.IntegerField()
    def __init__(self, *args, **kwargs):
        namefield=kwargs.pop('namefield', None)
        if namefield is not None:
            self.fields['name'] =  serializers.CharField(source=namefield)
        super(sumarySerializer,self).__init__(*args, **kwargs)


