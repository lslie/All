from django.shortcuts import render
from .models import Student,Class_grant,StudentId

# Create your views here.


def index(request):
    return render(request,'index.html')


def all_student(request):
    student = Student.objects.all()
    all_class = Class_grant.objects.all()
    return render(request,'all_student.html',{
        's':student,
        'all_class':all_class,
    })