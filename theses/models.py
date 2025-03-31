from django.db import models
from django.contrib.auth.models import User

class Thesis(models.Model):
    title_th = models.CharField(max_length=255, verbose_name="ชื่อวิทยานิพนธ์ (ไทย)")
    title_en = models.CharField(max_length=255, verbose_name="ชื่อวิทยานิพนธ์ (อังกฤษ)")

    student = models.ForeignKey(
        "students.Student",  # ใช้ string เพื่อเลี่ยง circular import
        on_delete=models.CASCADE,
        related_name="theses"
    )

    advisor = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='main_advised_theses',
        verbose_name="อาจารย์ที่ปรึกษาหลัก"
    )

    STATUS_CHOICES = [
        ('draft', 'ร่าง'),
        ('submitted', 'ส่งแล้ว'),
        ('under_review', 'อยู่ระหว่างตรวจสอบ'),
        ('approved', 'อนุมัติแล้ว'),
        ('rejected', 'ไม่ผ่าน'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title_th} ({self.student.user.first_name} {self.student.user.last_name})"

    class Meta:
        verbose_name = "Thesis"
        verbose_name_plural = "Theses"
