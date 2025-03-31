from django.urls import path
from .views import UserCreateAPIView

urlpatterns = [
    path('', UserCreateAPIView.as_view(), name='create-user'),
]
