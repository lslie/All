from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import UserRegisterForm,UserLoginForm
from .models import UserProFile
from articles.models import ArticleInfo,TagInfo
# Create your views here.


def index(request):
    all_articles = ArticleInfo.objects.all()


    #排行
    click_num = all_articles.order_by('-click_num')[:6]
    love_num = all_articles.order_by('-love_num')[:6]


    #获取标签
    tag_all = TagInfo.objects.all()
    tagid = request.GET.get('tagid','')
    #归档
    date_time = all_articles.datetimes('add_time','day',order='DESC')
    year = request.GET.get('year','')
    month = request.GET.get('month','')
    day = request.GET.get('day','')
    if year and month and day:
        all_articles = all_articles.filter(add_time__year=year,add_time__month=month,add_time__day=day)
        all_articles_set = set(all_articles)
    if tagid:
        tag = TagInfo.objects.filter(id=int(tagid))[0]
        all_articles = tag.article.all()
        all_articles_set1 = set(all_articles)
    try:
        a = list(all_articles_set & all_articles_set1)
        if a:
            all_articles = a
    except:
        pass


    #分页
    pa = Paginator(all_articles,2)
    page_num = request.GET.get('page_num',1)
    try:
        pages = pa.page(page_num)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request,'index.html',{
        'all_articles':pages,
        'click_num':click_num,
        'love_num':love_num,
        'tag_all':tag_all,
        'tagid':tagid,
        'date_time':date_time,
        'year':year,
        'month':month,
        'day':day,

    })


#注册函数
def user_register(request):
    if request.method =='GET':
        return render(request,'user_register.html')
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            #clear_data是一个字典
            username = user_register_form.cleaned_data['username']
            email = user_register_form.cleaned_data['email']
            url = user_register_form.cleaned_data['url']
            password = user_register_form.cleaned_data['password']
            password1 = user_register_form.cleaned_data['password1']
            user = UserProFile.objects.filter(username=username)
            if user:
                return render(request,'user_register.html',{
                    'msg':'用户已存在'
                })
            else:
                if password == password1:
                    a = UserProFile()
                    a.username = username
                    a.url = url
                    a.email = email
                    a.password = password
                    a.set_password(password)
                    a.save()
                    return redirect(reverse('index'))
                else:
                    return render(request, 'user_register.html', {
                        'msg': '密码不一致'
                    })
        else:
            return render(request,'user_register.html',{
                'user_register_form':user_register_form
            })



#登录
def user_login(request):
    if request.method == 'GET':
        return render(request,'user_login.html')
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            username = user_login_form.cleaned_data['username']
            password = user_login_form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect(reverse('index'))
            else:
                return render(request,'user_login.html',{
                    'msg':'用户或者密码错误'
                })
        else:
            return render(request,'user_login.html',{
                'user_login_form':user_login_form
            })

#显示个人信息详情
def user_date(request):
    #all_date = UserProFile.objects.filter(request.user)
    return render(request,'user_date.html',{
        'all_date':request.user
    })


#退出
def user_logout(request):
    logout(request)
    return redirect(reverse('index'))


#个人信息个人修改
def user_update(request):
    pass