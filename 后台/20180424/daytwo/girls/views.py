from django.shortcuts import render,HttpResponse

# Create your views here.


def girls_index(request):
    return render(request,'girls_index.html')

def get_girls_data(request):

    name = request.GET.get('name',None)
    age = request.GET.get('a',None)
    num = request.GET.get('b',None)
    str = '姓名'+name+'年龄'+age+'测试数据'+num
    return HttpResponse(str)


def from_test(request):
    if request.method == 'GET':
        return render(request,'from_test.html')
    else:
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        return HttpResponse(username +'------'+password)