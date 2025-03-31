from django.shortcuts import render
from rest_framework import viewsets
from .models import Department, Program, ProgramAdvisor
from .serializers import DepartmentSerializer, ProgramSerializer, ProgramAdvisorSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'code']
    ordering_fields = ['name']


class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department', 'degree_type']
    search_fields = ['name', 'code']
    ordering_fields = ['name']


class ProgramAdvisorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProgramAdvisor.objects.all()
    serializer_class = ProgramAdvisorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['program', 'advisor', 'is_program_chair']
    ordering_fields = ['start_date']
# Create your views here.
