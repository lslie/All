from django.shortcuts import render,HttpResponse

# Create your views here.


def girls_index(request):
    return render(request,'girls_index.html')

def get_girls_data(request):
    name = request.GET.get('name',None)
    age = request.GET.get('age',None)
    el = request.GET.get('el',None)
    #str =
    return HttpResponse('姓名'+name+'年龄'+age+'罪状'+el)

def from_test(request):
    if request.method == 'GET':
        return render(request,'from_test.html')
    else:
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        str = '用户名'+username+'密码'+password
        return HttpResponse(str)