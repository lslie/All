from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,'index.html')

def user_sin(request):
    if request.method == 'GET':
        return render(request,'user_sin.html')
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        password1 = request.POST.get('password1','')
        if password == password1:
            user = User()
            if user.username == username:
                return render(request,'user_sin.html',{
                    'msg':'用户已存在'
                })
            else:
                user.username = username
                user.password = password
                user.set_password(password)
                user.save()
                return render(request,'login.html')
        else:
            return render(request,'user_sin.html',{
                'msg':'用户密码输入不一致'
            })

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        return redirect(reverse('index'))