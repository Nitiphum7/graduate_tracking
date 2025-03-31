from django.contrib import admin
from .models import Thesis

@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = (
        'title_th',
        'get_student_name',
        'get_advisor_name',
        'status',
        'created_at',
    )

    def get_student_name(self, obj):
        return f"{obj.student.user.first_name} {obj.student.user.last_name}"
    get_student_name.short_description = 'STUDENT'

    def get_advisor_name(self, obj):
        if obj.advisor:
            return f"{obj.advisor.first_name} {obj.advisor.last_name}"
        return "-"
    get_advisor_name.short_description = 'อาจารย์ที่ปรึกษาหลัก'
