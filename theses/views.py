from django.shortcuts import render, get_object_or_404
from .models import Thesis
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView

def thesis_list(request):
    theses = Thesis.objects.all()
    advisors = User.objects.all()  # หรือ filter เฉพาะกลุ่มอาจารย์ก็ได้
    print("✅ Theses:", theses.count())
    return render(request, 'theses/list.html', {
        'theses': theses,
        'advisors': advisors,
    })


def thesis_detail(request, thesis_id):
    thesis = get_object_or_404(Thesis, pk=thesis_id)
    return render(request, 'theses/detail.html', {'thesis': thesis})

class ThesisListView(ListView):
    model = Thesis
    template_name = 'theses/list.html'
    context_object_name = 'theses'

class ThesisDetailView(DetailView):
    model = Thesis
    template_name = 'theses/detail.html'
    context_object_name = 'thesis'