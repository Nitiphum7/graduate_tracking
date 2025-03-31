from django.urls import path
from . import views

urlpatterns = [
    path('theses/', views.thesis_list, name='thesis_list'),
    path('theses/<int:pk>/', views.thesis_detail, name='thesis_detail'),  # ถ้ามีหน้า detail
]
