from django.contrib import admin
from .models import ClassInfo,StudentInfo,StudentId
# from admin_user import

# Register your models here.

class ClassInfoAdmin(admin.ModelAdmin):
    list_display = ['name','add_time']
    list_per_page = 2
    search_fields = ['name','add_time']
    list_filter = ['name']
    fields = ['name','add_time']


class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ['name','age','gender','add_time','th_class']
    list_per_page = 2
    search_fields = ['name', 'age','gender','add_time']
    list_filter = ['name', 'age','gender']
    fields = ['name', 'age','gender','add_time','th_class']
class StudentIdAdmin(admin.ModelAdmin):
    list_display = ['stu_id', 'add_time','th_stu']
    list_per_page = 2
    search_fields = ['stu_id', 'add_time']
    list_filter = ['stu_id']
    fields = ['stu_id', 'add_time','th_stu']
admin.site.register(ClassInfo,ClassInfoAdmin)
admin.site.register(StudentInfo,StudentInfoAdmin)
admin.site.register(StudentId,StudentIdAdmin)