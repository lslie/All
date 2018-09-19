import re

from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.shortcuts import render,redirect

# Create your views here.
from user.models import Passport



def register(request):
    if request.method == 'GET':
        return render(request,'register.html')

    else:
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        password1 = request.POST.get('cpwd')
        email = request.POST.get('email')
        # all方法进行数据校验，如果里面任意值为空，就不通过校验
        if not all([username,password,password1,email]):
            return render(request, 'register.html', {
                'msg':'不能输入有空的参数'
            })

        if not re.match(r'[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'msg':'输入的邮箱不正确'})

        # 通过向数据库添加用户信息
        passport = Passport.object.add_user(username=username, password=password, email=email)
        
        return redirect(reverse('index'), {'cmsg':'注册成功'})

# 用户登录校验
def login(request):
    if request.method == 'GET':
        # if request.COOKIES.get("usename"):
        if request.COOKIES.get("username"):
            username = request.COOKIES.get("username")
            checked = True
        else:
            username = ''
            checked = ''
        context = {
            'username': username,
            'checked' : checked,
        }
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        # 此时post取的是前段ajax数据并不是表单数据因为表单已经删除
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        remember = request.POST.get('remember')

        # 数据校验
        if not all([username, password]):
            # 数据为空
            return JsonResponse({'res': 2})
        passport = Passport.object.find_user(username=username,password=password)

        if passport:
            # next_url = request.session.get('url_path', reverse('index'))
            next_url = '/'
            print('---------------')
            jire = JsonResponse({'res': 1, 'next_url': next_url})
            if remember == 'true':
                # 记住用户名并设置cookie的保存时间
                jire.set_cookie('username', username, max_age=1*24*3600)
            else:
                # 不要记住用户名并删除cookie
                jire.delete_cookie('username')
            # 记住用户名的状态
            request.session['islogin'] = True
            request.session['username'] = username
            request.session['passport_id'] = passport.id
            return jire
        else:

            return JsonResponse({'res': 0})

def logout(request):
    '''用户退出操作'''
    # 清空用户session数据
    request.session.flush()
    # 然后跳转首页
    return redirect(reverse('index'))
