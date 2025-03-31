from django.shortcuts import render
from rest_framework import viewsets
from .models import Advisor
from .serializers import AdvisorSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from courses.models import Program


class AdvisorViewSet(viewsets.ModelViewSet):
    queryset = Advisor.objects.select_related('user', 'program').all()
    serializer_class = AdvisorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department']
    search_fields = ['user__first_name', 'user__last_name', 'field_of_expertise']
    ordering_fields = ['user__last_name', 'department']

