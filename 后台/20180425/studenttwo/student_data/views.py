from django.shortcuts import render,HttpResponse
from student_data.models import StudentInfo

# Create your views here.


def index(request):
    return render(request,'index.html')

def student_index(request):
    return render(request,'student_index.html')

#注册页面
def student_loge(request):
    if request.method == 'GET':
        return render(request,'student_loge.html')
    else:
        name = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        we_cat = request.POST.get('we_cat')
        class_college = request.POST.get('class_college')
        address = request.POST.get("address")
        StudentInfo.objects.create(name=name,age=age,gender=gender,we_cat=we_cat,class_college=class_college,address=address)

        return HttpResponse('提交成功')

#显示全部学生信息页面
def student_all(request):
    student = StudentInfo.objects.all()
    return render(request,'student_all.html',{
        's':student
    })