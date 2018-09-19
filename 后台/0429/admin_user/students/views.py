from django.shortcuts import render,redirect,Http404
from django.core.urlresolvers import reverse
from .models import StudentInfo,ClassInfo,StudentId
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/user/user_login/')
def student_list(request):
    all_student = StudentInfo.objects.all()
    return render(request,'student_list.html',{
        'all_student':all_student
    })
@login_required(login_url='/user/user_login/')
def student_delete(request,stu_id):
    if stu_id:
        #pk代表主键
        student = StudentInfo.objects.filter(pk=int(stu_id))[0]
        student.studentid.delete()
        student.delete()
        return redirect(reverse('students:student_list'))
    else:
        return Http404
@login_required(login_url='/user/user_login/')
def student_update(request,stu_id):
    if request.method =='GET':
        if stu_id:
            all_ban  = ClassInfo.objects.all()
            student = StudentInfo.objects.filter(pk=int(stu_id))[0]
            return render(request,'student_update.html',{
                'student':student,
                'all_ban':all_ban
            })
        else:
            if stu_id:
                student = StudentInfo.objects.filter(pk=int(stu_id))[0]
                stuname = request.POST.get('stuname','')
                stuage = request.POST.get('stuage','')
                stugender = request.POST.get('stugender','')
                stuuid = request.POST.get('stuuid','')
                stuban = request.POST.get('selected','')
                ban = ClassInfo.objects.filter(name=stuban)[0]
                student.name = stuname
                student.age = stuage
                student.gender = stugender
                student.th_class_id = ban.id
                student.save()
                student.studentid.id = stuuid
                student.studentid.save()
                return redirect(reverse('students:student_list'))
@login_required(login_url='/user/user_login/')
def student_add(request):
    if request.method == 'GET':
        all_ban = ClassInfo.objects.all()
        return render(request,'student_add.html',{
            'all_ban': all_ban
        })
    else:
        stuname = request.POST.get('stuname', '')
        stuage = request.POST.get('stuage', '')
        stugender = request.POST.get('stugender', '')
        stuuid = request.POST.get('stuuid', '')
        stuban = request.POST.get('selected', '')
        ban = ClassInfo.objects.filter(name=stuban)[0]
        student = StudentInfo()
        student.name = stuname
        student.age = stuage
        student.gender = stugender
        student.th_class_id = ban.id
        student.save()

        stu = StudentId()
        stu.stu_id = stuuid
        stu.th_stu = student.id
        stu.save()
        return render(request,'student_list.html')