from rest_framework import serializers
from .models import Advisor
from django.contrib.auth.models import User
from courses.models import Program


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'name', 'degree_type']

class AdvisorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    program = serializers.PrimaryKeyRelatedField(queryset=Program.objects.all(), allow_null=True)

    class Meta:
        model = Advisor
        fields = [
            'id', 'user', 'academic_title', 'field_of_expertise',
            'department', 'office_location', 'phone_number', 'program'
        ]