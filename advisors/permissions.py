from rest_framework import permissions

class IsAdvisorOrReadOnly(permissions.BasePermission):
    """
    อนุญาตให้อาจารย์ที่ปรึกษาแก้ไขข้อมูลของตัวเองได้
    """
    def has_object_permission(self, request, view, obj):
        # อ่านได้เสมอ
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # เขียนได้เฉพาะข้อมูลของตัวเอง
        return hasattr(request.user, 'advisor_profile') and obj.id == request.user.advisor_profile.id
