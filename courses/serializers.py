from rest_framework import serializers
from .models import Department, Program, ProgramAdvisor
from advisors.serializers import AdvisorSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'code']


class ProgramSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    degree_type_display = serializers.CharField(source='get_degree_type_display', read_only=True)
    
    class Meta:
        model = Program
        fields = ['id', 'name', 'code', 'department', 'degree_type', 'degree_type_display', 'credits_required', 'description']


class ProgramAdvisorSerializer(serializers.ModelSerializer):
    advisor = AdvisorSerializer(read_only=True)
    program = ProgramSerializer(read_only=True)
    
    class Meta:
        model = ProgramAdvisor
        fields = ['id', 'program', 'advisor', 'is_program_chair', 'start_date', 'end_date']
