from django.contrib import admin
from django.contrib import admin
from .models import Student, EnglishExamResult
from .models import Student

class EnglishExamResultInline(admin.TabularInline):
    model = EnglishExamResult
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'user', 'program', 'enrollment_date', 'status', 'advisor')
    list_filter = ('program', 'status', 'enrollment_date')
    search_fields = ('student_id', 'user__first_name', 'user__last_name')
    inlines = [EnglishExamResultInline]
    
    fieldsets = (
        ('ข้อมูลพื้นฐาน', {
            'fields': ('user', 'student_id', 'program', 'status')
        }),
        ('ข้อมูลการศึกษา', {
            'fields': ('enrollment_date', 'expected_graduation_date', 'advisor', 'co_advisor')
        }),
    )


@admin.register(EnglishExamResult)
class EnglishExamResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam_type', 'exam_date', 'score', 'status')
    list_filter = ('exam_type', 'status', 'exam_date')
    search_fields = ('student__student_id', 'student__user__first_name', 'student__user__last_name')
# Register your models here.
