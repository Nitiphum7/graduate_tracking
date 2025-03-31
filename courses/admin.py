from django.contrib import admin
from django.contrib import admin
from .models import Department, Program, ProgramAdvisor


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'department', 'degree_type', 'credits_required')
    list_filter = ('department', 'degree_type')
    search_fields = ('name', 'code')


@admin.register(ProgramAdvisor)
class ProgramAdvisorAdmin(admin.ModelAdmin):
    list_display = ('program', 'advisor', 'is_program_chair', 'start_date', 'end_date')
    list_filter = ('program', 'is_program_chair')
    search_fields = ('program__name', 'advisor__user__first_name', 'advisor__user__last_name')
# Register your models here.
