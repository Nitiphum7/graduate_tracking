from rest_framework import serializers
from .models import ThesisProposal, ThesisCommittee, ThesisDefense
from students.serializers import StudentSerializer
from advisors.serializers import AdvisorSerializer


class ThesisCommitteeSerializer(serializers.ModelSerializer):
    advisor = AdvisorSerializer(read_only=True)
    
    class Meta:
        model = ThesisCommittee
        fields = ['id', 'advisor', 'is_chair']


class ThesisProposalSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    committee_members = ThesisCommitteeSerializer(many=True, read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = ThesisProposal
        fields = ['id', 'student', 'title', 'abstract', 'submission_date', 'exam_date', 
                  'status', 'status_display', 'comments', 'committee_members']


class ThesisDefenseSerializer(serializers.ModelSerializer):
    thesis_proposal = ThesisProposalSerializer(read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = ThesisDefense
        fields = ['id', 'thesis_proposal', 'defense_date', 'status', 'status_display', 
                  'comments', 'revision_due_date', 'final_submission_date']
