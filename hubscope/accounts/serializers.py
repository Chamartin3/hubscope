from rest_framework import serializers
from django.contrib.auth.models import Permission, Group
from rest_framework.serializers import ModelSerializer, Serializer
from   hubscope.accounts.models import User
from hubscope.reports.models import Position, Company

def password_validation(data):
    if not data.get('password') or not data.get('passwordconf'):
        raise serializers.ValidationError("Please add a password and a confirmation.")

    if data.get('password') != data.get('passwordconf'):
        raise serializers.ValidationError("The two passwords do not match.")
    data.pop('passwordconf')
    return data


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)

class PositionSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()
    class Meta:
        model = Position
        fields = ['company','name']

class PasswordSerializer(Serializer):
    password = serializers.CharField()
    passwordconf = serializers.CharField(write_only=True)

    def validate(self, data):
        # data['username'] = uuid.uuid4().hex[:30]
        return password_validation(data)

class UserStatusSerializer(ModelSerializer):
    model = User
    fields = 'is_active'

class UserSerializer(ModelSerializer):
    groups=GroupsSerializer(many=True, read_only=True)
    roles = PositionSerializer(many=True, read_only=True)
    fullname = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = '__all__'





class UserRegistrationSerializer(Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    passwordconf = serializers.CharField(write_only=True)
    group = serializers.CharField(write_only=True)
    company = serializers.ListField(child=serializers.CharField(), required=False, write_only=True)

    def validate(self, data):
        # data['username'] = uuid.uuid4().hex[:30]
        return password_validation(data)

    def  create(self, validated_data):
        group = validated_data.pop('group',None)
        company = []
        if group in ['Gerente', 'Registrador']:
            company = validated_data.pop('company',[])
        
        validated_data.update({'username':validated_data['username'].lower()})
        user = User.objects.create_user(**validated_data)
        if group is not None:
            g = Group.objects.get(name=group)
            user.groups.set([g])

        companies =[ Company.objects.get(name=c) for c in company ]
        for comp in companies:
            Position.objects.create(
                company=comp,
                person=user,
                name=group)

        return user

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        group = GroupsSerializer(instance.groups, many=True).data
        result = super(UserRegistrationSerializer, self).to_representation(instance)
        result.update({'groups':group})
        return result