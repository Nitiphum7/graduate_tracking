from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from advisors.views import AdvisorViewSet
from courses.views import DepartmentViewSet, ProgramViewSet, ProgramAdvisorViewSet
from students.views import StudentViewSet, EnglishExamResultViewSet, StudentCreateView
from exams.views import ThesisProposalViewSet, ThesisCommitteeViewSet, ThesisDefenseViewSet
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from graduate_tracking.views import dashboard_view
from students.views import StudentListView, StudentDetailView
from advisors.views import AdvisorListView, AdvisorDetailView
from theses.views import ThesisListView, ThesisDetailView

router = DefaultRouter() 
router.register(r'advisors', AdvisorViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'programs', ProgramViewSet)
router.register(r'program-advisors', ProgramAdvisorViewSet)
router.register(r'students', StudentViewSet)
router.register(r'english-exams', EnglishExamResultViewSet)
router.register(r'thesis-proposals', ThesisProposalViewSet)
router.register(r'thesis-committees', ThesisCommitteeViewSet)
router.register(r'thesis-defenses', ThesisDefenseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🌟 Token Login สำหรับ Postman
    path('api-token-auth/', obtain_auth_token),

    # API
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
    path('api/users/', include('users.urls')), 
    path('api/students/', StudentCreateView.as_view(), name='student-create'),

    # หน้า Login
    path('', auth_views.LoginView.as_view(template_name='index.html'), name='home'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

    # Auth URLs
    path('accounts/', include([
        path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
        path('password_change/', auth_views.PasswordChangeView.as_view(template_name='auth/password_change.html'), name='password_change'),
        path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='auth/password_change_done.html'), name='password_change_done'),
        path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'), name='password_reset'),
        path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), name='password_reset_confirm'),
        path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name='password_reset_complete'),
    ])),

    # Frontend (TemplateView)
    path('students/', include([
        path('', TemplateView.as_view(template_name='students/list.html'), name='student_list'),
        path('<int:pk>/', TemplateView.as_view(template_name='students/detail.html'), name='student_detail'),
    ])),
    path('advisors/', include([
        path('', TemplateView.as_view(template_name='advisors/list.html'), name='advisor_list'),
        path('<int:pk>/', TemplateView.as_view(template_name='advisors/detail.html'), name='advisor_detail'),
    ])),
    path('programs/', include([
        path('', TemplateView.as_view(template_name='programs/list.html'), name='program_list'),
        path('<int:pk>/', TemplateView.as_view(template_name='programs/detail.html'), name='program_detail'),
    ])),
    path('theses/', include([
        path('', TemplateView.as_view(template_name='theses/list.html'), name='thesis_list'),
        path('<int:pk>/', TemplateView.as_view(template_name='theses/detail.html'), name='thesis_detail'),
    ])),
    path('dashboard/', dashboard_view, name='dashboard'), 
]

path('students/', include([
    path('', StudentListView.as_view(), name='student_list'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
])),

path('advisors/', AdvisorListView.as_view(), name='advisor_list'),
path('advisors/<int:pk>/', AdvisorDetailView.as_view(), name='advisor_detail'),

path('theses/', ThesisListView.as_view(), name='thesis_list'),
path('theses/<int:pk>/', ThesisDetailView.as_view(), name='thesis_detail'),