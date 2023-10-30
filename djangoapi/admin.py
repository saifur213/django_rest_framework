from django.contrib import admin
from .models import Teacher
# Register your models here.
@admin.register(Teacher)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher_name', 'course_name', 'course_duration', 'seat']