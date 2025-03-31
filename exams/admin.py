from django.contrib import admin
from django.contrib import admin
from .models import ThesisProposal, ThesisCommittee, ThesisDefense


class ThesisCommitteeInline(admin.TabularInline):
    model = ThesisCommittee
    extra = 1


@admin.register(ThesisProposal)
class ThesisProposalAdmin(admin.ModelAdmin):
    list_display = ('student', 'title', 'submission_date', 'exam_date', 'status')
    list_filter = ('status', 'submission_date', 'exam_date')
    search_fields = ('student__student_id', 'student__user__first_name', 'student__user__last_name', 'title')
    inlines = [ThesisCommitteeInline]
    
    fieldsets = (
        ('ข้อมูลวิทยานิพนธ์', {
            'fields': ('student', 'title', 'abstract')
        }),
        ('ข้อมูลการสอบ', {
            'fields': ('submission_date', 'exam_date', 'status', 'comments')
        }),
    )


@admin.register(ThesisDefense)
class ThesisDefenseAdmin(admin.ModelAdmin):
    list_display = ('thesis_proposal', 'defense_date', 'status', 'revision_due_date', 'final_submission_date')
    list_filter = ('status', 'defense_date')
    search_fields = ('thesis_proposal__student__student_id', 'thesis_proposal__student__user__first_name', 
                     'thesis_proposal__student__user__last_name', 'thesis_proposal__title')
# Register your models here.
