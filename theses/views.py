from django.shortcuts import render, get_object_or_404
from .models import Thesis
from django.contrib.auth.models import User


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
