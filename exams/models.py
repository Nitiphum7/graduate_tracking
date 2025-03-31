from django.db import models
from django.db import models
from students.models import Student
from advisors.models import Advisor


class ThesisProposal(models.Model):
    STATUS_CHOICES = [
        ('pending', 'รอสอบ'),
        ('passed', 'ผ่าน'),
        ('passed_with_revision', 'ผ่านโดยมีการแก้ไข'),
        ('failed', 'ไม่ผ่าน'),
    ]
    
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='thesis_proposal')
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    submission_date = models.DateField()
    exam_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    comments = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.student} - {self.title}"


class ThesisCommittee(models.Model):
    thesis_proposal = models.ForeignKey(ThesisProposal, on_delete=models.CASCADE, related_name='committee_members')
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    is_chair = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['thesis_proposal', 'advisor']
    
    def __str__(self):
        role = "Chair" if self.is_chair else "Member"
        return f"{self.advisor} - {role}"


class ThesisDefense(models.Model):
    STATUS_CHOICES = [
        ('pending', 'รอสอบ'),
        ('passed', 'ผ่าน'),
        ('passed_with_revision', 'ผ่านโดยมีการแก้ไข'),
        ('failed', 'ไม่ผ่าน'),
    ]
    
    thesis_proposal = models.OneToOneField(ThesisProposal, on_delete=models.CASCADE, related_name='thesis_defense')
    defense_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    comments = models.TextField(blank=True, null=True)
    revision_due_date = models.DateField(null=True, blank=True)
    final_submission_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.thesis_proposal.student} - Defense"
# Create your models here.
