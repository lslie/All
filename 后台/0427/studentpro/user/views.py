from django.shortcuts import render,redirect
from .models import Student,Student_Id,Class_grade
from django.core.urlresolvers import reverse

# Create your views here.


def index(request):
    return render(request,'index.html')

#查看所有获取学生班级学生学号学生信息
def all_student(request):
    student = Student.objects.all()
    return render(request,'all_student.html',{
        's':student
    })


#删除首先要删除学生的学号然后删除学生
def delete_student(request,stu_no):
    if stu_no:
        student = Student.objects.filter(id=int(stu_no))[0]
        if student.name:
            #student.student_id.delete()
            student.delete()
            return redirect(reverse('user:all_student'))
        else:
            student.delete()
            return redirect(reverse('user:all_student'))
    else:
        student = Student.objects.filter(request.GET.get('name',None))[0]
        student.delete()
        return redirect(reverse('user:all_student'))

#更新学生信息
def update_student(request,stu_no):
    if stu_no:
        if request.method=='GET':
            all_class = Class_grade.objects.all()
            stu = Student.objects.filter(id=int(stu_no))[0]

            return render(request,'update_student.html',{
                's':stu,
                'all_cla':all_class
            })
    else:
        if stu_no:
            stu_ban = request.POST.get('stu_ban',None)
            stu_name = request.POST.get('stu_name',None)
            stu_age = request.POST.get('stu_age',None)
            stu_gender = request.POST.get('stu_gender',None)
            stu_id = request.POST.get('stu_id',None)

            stu_class = Class_grade.objects.filter(name=stu_ban)[0]
            stu = Student.objects.filter(id=int(stu_no))[0]

            stu.name = stu_name
            stu.age =stu_age
            stu.gender = stu_gender
            stu.th_class_id=stu_class.id
            stu.save()

            stu.student_id.id=stu_id
            stu.student_id.save()
            return redirect(reverse('user:all_student'))


#注册学生信息
def login_student(request):
    if request.method=='GET':
        class_stu = Class_grade.objects.all()
        return render(request,'login_student.html',{
            'all_class':class_stu
        })
    else:
        stu_ban = request.POST.get('stu_class', None)
        stu_name = request.POST.get('stu_name', None)
        stu_age = request.POST.get('stu_age', None)
        stu_gender = request.POST.get('stu_gender', None)
        stu_id = request.POST.get('stu_id', None)
        stu_class = Class_grade.objects.filter(name=stu_ban)[0]
        student = Student()
        student.name = stu_name
        student.age = stu_age
        student.gender = stu_gender
        student.th_class_id =stu_class.id
        student.save()
        student_id = Student_Id()
        student_id.student_no = stu_id
        student_id.th_student_id = student.id
        student_id.save()
        return redirect(reverse('user:all_student'))