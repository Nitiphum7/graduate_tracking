from django.shortcuts import render
from students.models import Student
from courses.models import Program
from theses.models import Thesis

def dashboard_view(request):
    students = Student.objects.all()
    programs = Program.objects.all()
    theses = Thesis.objects.all()

    return render(request, 'dashboard.html', {
        'students': students,
        'programs': programs,
        'theses': theses,
    })
