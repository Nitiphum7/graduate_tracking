from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render



class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='advisor_profile')
    academic_title = models.CharField(max_length=50)
    field_of_expertise = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    office_location = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    program = models.ForeignKey('courses.Program', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.academic_title} {self.user.first_name} {self.user.last_name}"

def thesis_list(request):
    theses = theses.Thesis.objects.all()
    advisors = User.objects.all()  
    return render(request, 'theses/thesis_list.html', {
        'theses': theses,
        'advisors': advisors
    })
