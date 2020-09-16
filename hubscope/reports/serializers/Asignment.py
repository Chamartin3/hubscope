from rest_framework.serializers import ModelSerializer, Serializer, DateField, SerializerMethodField
from .Reports import  ReportSerializer
from .Indicator import  MetricSerializer

from hubscope.reports.models import Asignment

class AsignmentSerializer(ModelSerializer):
    last_end = DateField(required=False)
    deadline_date = DateField(read_only=True)
    first_report_date = DateField(read_only=True)
    active_goal = ReportSerializer(read_only=True)
    metric_info = MetricSerializer(read_only=True, source="metric")

    class Meta:
        model = Asignment
        fields =  [
            'id',
            'metric',
            'metric_info',
            'company',
            'last_begin',
            'last_end',
            'days_to_deliver',
            'metafreq',
            'frecuency',
            'periodic',
            'active_goal',
            'deadline_date',
            'total_genetated_reports',
            'reports_by_status',
            'first_report_date',
        ]
    # def get_first_report_date(self, asignment):
    #     return asignment.first_report.begin