from django.shortcuts import render,HttpResponse

# Create your views here.

def index():
    return HttpResponse("首页")
def show_news(request):
    return HttpResponse("新闻")

def show_world(request):
    a = 'zhaoliying'
    b = [1,2,3,4]
    c = {'name':'zhangxu','age':18}
    context = {
        'a':a,
        'b':b,
        'c':c
    }
    return render(request,'new_world.html',context)