from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from .models import UserProfile

# Create your views here.

def index(request):
    return render(request,'index.html')


def login_user(request):
    if request.method == 'GET':
        return render(request,'login_user.html')
    else:
        username = request.POST.get('username',None)
        nik_name = request.POST.get('nik_name','')
        password = request.POST.get('password',None)
        password1 = request.POST.get('password1',None)
        user = UserProfile.objects.filter(username=username)
        if user:
            return render(request,'login_user.html',{
                'msg':'用户名已存在请重新输入'
            })
        else:
            if password == password1:
                #必须实例化才能创建
                users =UserProfile()
                users.username = username
                users.password = password
                users.nik_name = nik_name
                users.save()
                return redirect(reverse('index'))


def register_user(request):
    return render(request,'register_user.html')