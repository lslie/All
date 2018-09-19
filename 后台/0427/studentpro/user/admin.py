from django.contrib import admin
from .models import Student,Student_Id,Class_grade

# Register your models here.

admin.site.register(Student)
admin.site.register(Student_Id)
admin.site.register(Class_grade)