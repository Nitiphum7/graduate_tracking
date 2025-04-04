# Generated by Django 5.1.7 on 2025-03-27 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_program_department'),
        ('theses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_th', models.CharField(max_length=255, verbose_name='ชื่อวิทยานิพนธ์ (ไทย)')),
                ('title_en', models.CharField(max_length=255, verbose_name='ชื่อวิทยานิพนธ์ (อังกฤษ)')),
                ('status', models.CharField(choices=[('draft', 'ร่าง'), ('submitted', 'ส่งแล้ว'), ('under_review', 'อยู่ระหว่างตรวจสอบ'), ('approved', 'อนุมัติแล้ว'), ('rejected', 'ไม่ผ่าน')], default='draft', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theses', to='students.student')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
