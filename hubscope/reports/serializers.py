from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from hubscope.reports.models import Company, Asignment, Indicator, Report, CompanyRole


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ['name','desc']


class AsignmentSerializer(ModelSerializer):
    class Meta:
        model = Asignment
        fields =  [
            'name',
            'company',
            'last',
            'frecuency',
        ]

class IndicatorSerializer(ModelSerializer):
    class Meta:
        model = Indicator
        fields = ['name','tipo'] 

class ReportSerializer(ModelSerializer):
    value = serializers.SerializerMethodField(source="val")
    class Meta:
        model = Report
        fields = [
            'indicator',
            'asignment',
            'value',
            'created_at',
            'registered_by',
            'updated_at',
            'modified_by']
    def val(self, report):
        return report.val


class CompanyRoleSerializer(ModelSerializer):
    class Meta:
        model = CompanyRole
        fields = '__all__'
