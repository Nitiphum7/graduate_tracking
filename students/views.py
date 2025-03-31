from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Student, EnglishExamResult
from .serializers import StudentSerializer, EnglishExamResultSerializer
from .permissions import IsStudentOrAdvisorOrAdmin
from django.db import models
from django.contrib.auth.models import User  
from . import serializers  
from django.views.generic import ListView, DetailView
from .models import Student




class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

def perform_create(self, serializer):
    try:
        user = User.objects.get(id=self.request.data.get('user_id'))
        serializer.save()
    except User.DoesNotExist:
        raise serializers.ValidationError("User ID นี้ไม่มีในระบบ")


class StudentViewSet(viewsets.ModelViewSet): 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsStudentOrAdvisorOrAdmin]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['program', 'status', 'advisor']
    search_fields = ['student_id', 'user__first_name', 'user__last_name']
    ordering_fields = ['enrollment_date', 'student_id']
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Student.objects.all()
        if hasattr(user, 'advisor_profile'):
            advisor_id = user.advisor_profile.id
            return Student.objects.filter(
                models.Q(advisor_id=advisor_id) | models.Q(co_advisor_id=advisor_id)
            )
        if hasattr(user, 'student_profile'):
            return Student.objects.filter(id=user.student_profile.id)
        return Student.objects.none()

    def perform_create(self, serializer):
        print("🚀 Creating Student...")
        serializer.save()


class EnglishExamResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EnglishExamResult.objects.all()
    serializer_class = EnglishExamResultSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['student', 'exam_type', 'status']
    ordering_fields = ['exam_date']

class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'