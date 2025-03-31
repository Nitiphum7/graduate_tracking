from rest_framework import serializers
from .models import Student, EnglishExamResult
from django.contrib.auth.models import User
from courses.serializers import ProgramSerializer
from advisors.serializers import AdvisorSerializer
from users.serializers import UserSerializer

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    program = ProgramSerializer(read_only=True)
    advisor = AdvisorSerializer(read_only=True)
    co_advisor = AdvisorSerializer(read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
   
    # เพิ่ม field ให้สามารถรับค่าผ่าน API ได้
    user_id = serializers.IntegerField(write_only=True)
    program_id = serializers.IntegerField(write_only=True)
    advisor_id = serializers.IntegerField(write_only=True, required=False)
    co_advisor_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Student
        fields = [
            'id', 'user', 'user_id', 'student_id', 'program', 'program_id', 'enrollment_date', 
            'expected_graduation_date', 'status', 'status_display', 'advisor', 'advisor_id', 
            'co_advisor', 'co_advisor_id'
        ]

    def create(self, validated_data):
        """
        ฟังก์ชันนี้ใช้สร้าง Student ใหม่ โดยดึง user, program, advisor, co_advisor จาก ID ที่ส่งมา
        """
        user = User.objects.get(id=validated_data.pop('user_id'))
        program = validated_data.pop('program_id')
        advisor = validated_data.pop('advisor_id', None)
        co_advisor = validated_data.pop('co_advisor_id', None)

        student = Student.objects.create(
            user=user,
            program_id=program,
            advisor_id=advisor,
            co_advisor_id=co_advisor,
            **validated_data
        )
        return student
    
    def update(self, instance, validated_data):
        if 'user_id' in validated_data:
            instance.user = User.objects.get(id=validated_data.pop('user_id'))
        if 'program_id' in validated_data:
            instance.program_id = validated_data.pop('program_id')
        if 'advisor_id' in validated_data:
            instance.advisor_id = validated_data.pop('advisor_id')
        if 'co_advisor_id' in validated_data:
            instance.co_advisor_id = validated_data.pop('co_advisor_id')
        return super().update(instance, validated_data)




class EnglishExamResultSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    exam_type_display = serializers.CharField(source='get_exam_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = EnglishExamResult
        fields = ['id', 'student', 'exam_type', 'exam_type_display', 'exam_date', 'score', 'status', 'status_display']



