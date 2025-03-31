from django.shortcuts import render
from rest_framework import viewsets
from .models import Advisor
from .serializers import AdvisorSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from courses.models import Program
from django.views.generic import ListView, DetailView



class AdvisorViewSet(viewsets.ModelViewSet):
    queryset = Advisor.objects.select_related('user', 'program').all()
    serializer_class = AdvisorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department']
    search_fields = ['user__first_name', 'user__last_name', 'field_of_expertise']
    ordering_fields = ['user__last_name', 'department']

class AdvisorListView(ListView):
    model = Advisor
    template_name = 'advisors/list.html'
    context_object_name = 'advisors'

class AdvisorDetailView(DetailView):
    model = Advisor
    template_name = 'advisors/detail.html'
    context_object_name = 'advisor'