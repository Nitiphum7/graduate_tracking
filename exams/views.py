from django.shortcuts import render
from rest_framework import viewsets
from .models import ThesisProposal, ThesisCommittee, ThesisDefense
from .serializers import ThesisProposalSerializer, ThesisCommitteeSerializer, ThesisDefenseSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ThesisProposalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ThesisProposal.objects.all()
    serializer_class = ThesisProposalSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['student', 'status']
    search_fields = ['title', 'student__student_id', 'student__user__first_name', 'student__user__last_name']
    ordering_fields = ['submission_date', 'exam_date']


class ThesisCommitteeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ThesisCommittee.objects.all()
    serializer_class = ThesisCommitteeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['thesis_proposal', 'advisor', 'is_chair']


class ThesisDefenseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ThesisDefense.objects.all()
    serializer_class = ThesisDefenseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['thesis_proposal', 'status']
    ordering_fields = ['defense_date']
# Create your views here.
