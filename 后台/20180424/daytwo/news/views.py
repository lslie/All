from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    return render(request,'index.html')

def news_index(request):
    return render(request,'news_index.html')


def news_get(request,year,month,day):
    str = year+'年'+month+'月'+day+'日'
    return HttpResponse(str)