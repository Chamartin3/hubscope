from rest_framework.serializers import ModelSerializer,  SerializerMethodField, StringRelatedField

from hubscope.reports.serializers.Reports import ReportSerializer 
from hubscope.reports.serializers.Indicator import GoalStatusSerializer
from hubscope.reports.models import (
    Goal,
    Metric,
    Company, 
    Asignment, 
    Indicator, 
    Position,
    Report)
      



class CompanySerializer(ModelSerializer):
    # expected_reports = AsignmentSerializer(many=True)
    reports = ReportSerializer(many=True, read_only=True)
    open_goals = GoalStatusSerializer(many=True, read_only=True)
    # indicators = IndicatorSerializer(many=True) 
    class Meta:
        model = Company
        fields = [
            'id',
            'name', 
            'reports', 
            'open_goals'
            ]



class PositionSerializer(ModelSerializer):
    user = SerializerMethodField()
    company = StringRelatedField()
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
