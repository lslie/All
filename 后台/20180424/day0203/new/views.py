from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    return render(request,'index.html')


def new_index(request):
    return render(request,'new_index.html')
def get_data(request,year,month,day):

    return HttpResponse(year+month+day+'的新闻')