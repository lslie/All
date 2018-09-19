from django.shortcuts import render

from students_data.models import StudentInfo

# Create your views here.

def index(request):
    return render(request,'index.html')


def student_index(request):
    return render(request,'student_index.html')

def student_list(request):
    student = StudentInfo.objects.all()
    return render(request,'student_list.html',{
        'student':student
    })