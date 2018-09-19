from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import UserProFile

# Create your views here.


def index(request):
    #通过session找到u_name的值
    u_name = request.session.get('u_name',None)
    #通过cookiec找到
    #u_name = request.COOKIES.get('u_name',None)
    return render(request,'index.html',{
        'u_name':u_name
    })

#登录
def user_login(request):
    if request.method == 'GET':
        u_name = request.COOKIES.get('u_name',None)
        return render(request,'user_login.html',{
            'u_name':u_name
        })
    else:
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        check = request.POST.get('check',None)
        password1 = request.POST.get('password1',None)
        user = UserProFile.objects.filter(username=username)
        if user:
            if password == user[0].password:
                #设置session
                request.session['u_name'] = username
                if check:
                    ret = HttpResponseRedirect(reverse('index'))
                    ret.set_cookie('u_name',username,max_age=100)
                    return ret
                else:
                    ret = HttpResponseRedirect(reverse('index'))
                    ret.delete_cookie('u_name')
                    return ret
            else:
                return render(request,'user_login.html',{
                    'msg':'密码错误'
                })
        else:
            return render(request,'user_login.html',{
                'msg':'用户不存在'
            })


#注册
def user_register(request):
    if request.method == 'GET':
        return render(request,'user_register.html')
    else:
        username = request.POST.get('username', None)
        nik_name = request.POST.get('nik_name', None)
        password = request.POST.get('password', None)
        password1 = request.POST.get('password1', None)
        user = UserProFile.objects.filter(username=username)
        if user:
            return render(request, 'user_register.html', {
                'msg': '用户已存在'
            })
        else:
            user = UserProFile()
            user.username = username
            user.nik_name = nik_name
            if password1 != password:
                return render(request,'user_register.html',{
                    'msg':'两次密码不一致'
                })
            else:
                user.password = password
                user.save()
                return redirect(reverse('index'))

#注销
def user_logout(request):
    request.session.clear()
    ret = HttpResponseRedirect(reverse('index'))
    ret.delete_cookie('u_name')
    return ret

#退出
def user_delete(request):
    request.session.clear()
    return redirect(reverse('index'))