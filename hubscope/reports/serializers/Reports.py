from rest_framework.serializers import ModelSerializer, Serializer, SerializerMethodField, BooleanField

from hubscope.accounts.models import User
from hubscope.reports.models import  Report

from .Indicator import  MetricSerializer

class ReportDeliverySerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = ['value']
            


class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','fullname','last_login']    




    
class ReportSerializer(ModelSerializer):
    name = SerializerMethodField()
    unidad = SerializerMethodField()
    company_name = SerializerMethodField()
    # end = SerializerMethodField()
    metric = MetricSerializer()
    registered_by = UserInfoSerializer(read_only=True)
    modified_by = UserInfoSerializer(read_only=True)
    editable = BooleanField(required=False)
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
            'company_name',
            'deadline',
            'editable',
            'unidad',
            'created_at',
            'registered_by',
            'updated_at',
            'modified_by']

    def get_valor(self, report):
        return report.value        
    
    # def get_end(self, report):
    #     return report.dayrange.end    

    def get_name(self, report):
        return report.metric.name

    def get_unidad(self, report):
        return report.metric.unidad

    def get_company_name(self, report):
        if not report.company:
            return ''
        return report.company.name
