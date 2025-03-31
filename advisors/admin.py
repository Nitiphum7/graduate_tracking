from django.contrib import admin
from django.contrib import admin
from .models import Advisor


@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'academic_title', 'department', 'field_of_expertise')
    list_filter = ('department',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'field_of_expertise')
# Register your models here.
