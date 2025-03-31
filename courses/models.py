from django.db import models
from django.db import models



class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.name


class Program(models.Model):
    DEGREE_CHOICES = [
        ('Masters', 'ปริญญาโท'),
        ('Doctoral', 'ปริญญาเอก'),
    ]
    
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs')
    degree_type = models.CharField(max_length=20, choices=DEGREE_CHOICES)
    credits_required = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} ({self.get_degree_type_display()})"


class ProgramAdvisor(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='program_advisors')
    advisor = models.ForeignKey("advisors.Advisor", on_delete=models.CASCADE, related_name='advised_programs')
    is_program_chair = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    class Meta:
        unique_together = ['program', 'advisor']
    
    def __str__(self):
        return f"{self.advisor} - {self.program}"
# Create your models here.
