from django.db import models
from django.db import models
from django.contrib.auth.models import User
from advisors.models import Advisor
from courses.models import Department 

class Student(models.Model):
    STATUS_CHOICES = [
        ('active', 'กำลังศึกษา'),
        ('leave', 'ลาพัก'),
        ('graduated', 'จบการศึกษา'),
        ('terminated', 'พ้นสภาพ'),
    ]
    
    student_id = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    program = models.ForeignKey("courses.Program", on_delete=models.CASCADE, related_name='students')
    enrollment_date = models.DateField()
    expected_graduation_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    advisor = models.ForeignKey(Advisor, on_delete=models.SET_NULL, null=True, blank=True, related_name='advised_students')
    co_advisor = models.ForeignKey(Advisor, on_delete=models.SET_NULL, null=True, blank=True, related_name='co_advised_students')
    
    def __str__(self):
        return f"{self.student_id}: {self.user.first_name} {self.user.last_name}"


class EnglishExamResult(models.Model):
    EXAM_TYPE_CHOICES = [
        ('TOEFL', 'TOEFL'),
        ('IELTS', 'IELTS'),
        ('CU-TEP', 'CU-TEP'),
        ('TU-GET', 'TU-GET'),
    ]
    
    STATUS_CHOICES = [
        ('pass', 'ผ่าน'),
        ('fail', 'ไม่ผ่าน'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='english_exam_results')
    exam_type = models.CharField(max_length=10, choices=EXAM_TYPE_CHOICES)
    exam_date = models.DateField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)
    
    def __str__(self):
        return f"{self.student} - {self.exam_type}: {self.score}"
# Create your models here.

class Program(models.Model):
    name = models.CharField(max_length=255, unique=True)  # ชื่อหลักสูตร
    description = models.TextField(blank=True, null=True)  # รายละเอียดหลักสูตร
    credits_required = models.IntegerField(default=140)  # หน่วยกิตที่ต้องเรียนจบ
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
       return self.name

