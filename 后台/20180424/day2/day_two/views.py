from django.shortcuts import render,HttpResponse,loader,RequestContext


# Create your views here.
#使用
def book(request):
    a = '张旭'
    b = ['刘备', '关羽', '张飞']
    c = {'name': '潘金莲', 'age': '100'}
    text_cont = {
        'a': a,
        'b': b,
        'c': c
    }
    return render(request, 'atguigu.html', text_cont)
