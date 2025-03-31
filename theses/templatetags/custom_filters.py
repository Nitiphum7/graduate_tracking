# theses/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def status_badge_color(status):
    if status == "ผ่าน":
        return "success"
    elif status == "ไม่ผ่าน":
        return "danger"
    elif status == "รอตรวจ":
        return "warning"
    return "secondary"
