from rest_framework import serializers
from django.contrib.auth.models import Permission, Group
from rest_framework.serializers import ModelSerializer, Serializer
from   hubscope.accounts.models import User


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

    def validate(self, data):
        # data['username'] = uuid.uuid4().hex[:30]
        return password_validation(data)

    def  create(self, validated_data):
        group=validated_data.pop('group',None)
        validated_data.update({'username':validated_data['username'].lower()})
        user= User.objects.create_user(**validated_data)
        if group is not None:
            g=Group.objects.get(name=group)
            user.groups.set([g])
        return user

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        group = GroupsSerializer(instance.groups, many=True).data
        result = super(UserRegistrationSerializer, self).to_representation(instance)
        result.update({'groups':group})
        return result