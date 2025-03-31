from rest_framework import permissions

class IsStudentOrAdvisorOrAdmin(permissions.BasePermission):
    """
    อนุญาตให้นักศึกษาดูข้อมูลของตัวเอง หรืออาจารย์ที่ปรึกษาดูข้อมูลของนักศึกษาในที่ปรึกษา
    """
    def has_object_permission(self, request, view, obj):
        # Admin access
        if request.user.is_staff:
            return True
        
        # Student access (own profile)
        if hasattr(request.user, 'student_profile') and obj.id == request.user.student_profile.id:
            return True
        
        # Advisor access (advisees)
        if hasattr(request.user, 'advisor_profile'):
            return obj.advisor_id == request.user.advisor_profile.id or obj.co_advisor_id == request.user.advisor_profile.id
        
        return False
