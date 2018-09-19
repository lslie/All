from django.shortcuts import render

# Create your views here.


def  index(request):
    return render(request,'index.html')

def mains_index(request):
    return render(request,'mains_index.html')